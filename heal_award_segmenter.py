import csv
import requests
import collections
import re

def main():
    # Create Project Number List
    filepath = "inputs/awarded_08_DEC_2021.csv"
    project_num_list,core_project_num_list = create_project_num_list_from_csv(filepath) # add core project num list
    results = post_request(project_num_list)
    pub_results = post_request(core_project_num_list, "publications/search")

    # Projects not in reporter
    projects_not_in_reporter = []
    results_project_nums = [x['project_num'] for x in results]
    for project in project_num_list:
        if project not in results_project_nums:
            projects_not_in_reporter.append(project)

    with open("outputs/projects_not_in_reporter_08_DEC_2021.txt", "w") as f:
            for project in projects_not_in_reporter:
                f.write("%s\n" % project)

    # Map flatten function to results
    results_flat = list(map(flatten_json, results))
    fieldnames = []
    for result in results_flat:
        fieldnames.extend(list(result.keys()))
    fieldnames = list(set(fieldnames))

    # Write flattened results dicts to CSV
    with open('outputs/heal_awards_08_DEC_2021.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results_flat:
            writer.writerow(result)

    # Write publications results dicts to CSV
    with open('outputs/heal_award_pubs_08_DEC_2021.csv', 'w', newline='') as csvfile:
        fieldnames = []
        for result in pub_results:
            fieldnames.extend(list(result.keys()))
        fieldnames = list(set(fieldnames))
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in pub_results:
            writer.writerow(result)

def create_project_num_list_from_txt(txt_filepath,header=True):
    '''
    create_project_num_list_from_txt takes a newline-separated .txt file with 
    project numbers that may optionally have a header and returns a 
    list object of project numbers.
    '''
    project_num_list = []

    with open(txt_filepath, "r") as f:
        lines = f.readlines()
        lines = lines[1:] if header else lines
        for line in lines:
            if line=="\n":
                continue # skip if blank line
            line = line.strip()
            project_num_list.append(line)
    
    return(project_num_list)

def create_project_num_list_from_csv(csv_filepath):
    '''
    create_project_num_list_from_csv takes the 'awarded.csv' file from https://heal.nih.gov/funding/awarded
    and returns 2 separate list objects of project numbers and core project numbers.  For debugging purposes, it also
    returns a list of project titles that do not have a project number associated.
    '''
    project_num_list = []
    missing_nums_list = []
    

    with open(csv_filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            project_number = re.sub(r'[^\x00-\x7F]', '',row['proj_num']).replace(" ","") # eliminate non UTF-8 characters
            project_title = re.sub(r'[^\x00-\x7F]', '', row['proj_tittle']).replace(" ","") # eliminate non UTF-8 characters
            if row['proj_num'] == "":
                missing_nums_list.append(project_title.strip())
            else:
                project_num_list.append(project_number.strip())
        
    # Get core_project_num_list using re
    core_project_num_list = list(map(lambda x: re.sub("^[0-9]+","",x), project_num_list)) # remove beginning
    core_project_num_list = list(map(lambda x: re.match(".+(?=-)|[^-]+",x).group(0), core_project_num_list)) # find last instance of '-' and remove.

    # Write to projects
    with open("outputs/projects_with_missing_nums_08_DEC_2021.txt", "w") as f:
        for title in missing_nums_list:
            f.write("%s\n" % title)


    return(project_num_list,core_project_num_list)

def post_request(project_num_list, end_point = "projects/search", chunk_length=50):
    '''
    post_request hits the NIH reporter API end point and returns a list of results.
    Currently, the request body is hardcoded.  We could abstract out if needed.
    We split up API requests in increments equal to 'chunk_length' to avoid errors.
    '''
    # Add Wildcard Search
    #project_search_list = list(map(lambda x: re.match(".+(?=-)|[^-]+",x).group(0) + "*", project_num_list))

    # Initialize Results List
    results_list = []
    criteria_name = "project_nums" if end_point == "projects/search" else "core_project_nums"

    # Request Details
    base_url = "https://api.reporter.nih.gov/v2/"
    url = f"{base_url}{end_point}"
    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
        }

    for i in range(0,len(project_num_list),chunk_length):
        projects = project_num_list[i:i+chunk_length]

        # Request Body
        request_body = {
            
            "criteria":
            {
                #"include_active_projects": "true",
                criteria_name: projects
            },
            "offset":0,
            "limit":500
        }

        # Request Object
        req = requests.request(method = 'POST',
                            url = url,
                            headers = headers, 
                            json = request_body)

        # Append list of JSON results
        results_list.extend(req.json()['results'])
    
    return(results_list)

def flatten_json(dictionary, parent_key=False, separator='.'):
    # https://github.com/ScriptSmith/socialreaper/blob/master/socialreaper/tools.py
    '''
    Turn a nested dictionary into a flattened dictionary
    :param dictionary: The dictionary to flatten
    :param parent_key: The string to prepend to dictionary's keys
    :param separator: The string used to separate flattened keys
    :return: A flattened dictionary
    '''

    items = []
    for key, value in dictionary.items():
        if value==None: # skip if None
            continue
        new_key = str(parent_key) + separator + key if parent_key else key

        if isinstance(value, collections.MutableMapping):
            items.extend(flatten_json(value, new_key, separator).items()) #recurse

        elif isinstance(value, list):
            if not value: #skip list if empty
                continue
            elif isinstance(value[0], dict):
                items.extend(flatten_json(merge_dict(value), new_key, separator).items()) #recurse
            else:
                value = '; '.join(map(str,value))
                items.append((new_key, value)) # append as tuple
            
        else:
            items.append((new_key, value)) # append as tuple
    return dict(items)

def merge_dict(dict_list):
    '''
    Merges dictionaries in a list by turning values of same keys into a 
    list of values in the target dictionary.
    '''
    d_new = {}
    for d in dict_list:
        for k,v in d.items():
            if k in d_new:
                d_new[k].append(v)
            else:
                d_new[k] = [v]
    return(d_new)

if __name__ == "__main__":
    main()


