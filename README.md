# NIH RePORTER Query Script
This repository contains an input file, a python script, and a bash script which, when executed, reads the project IDs found in the input file, queries the NIH RePORTER API using these IDs, and outputs 4 files:

- `heal_awards.csv` - a table of the HEAL awards and associated information from the NIH RePORTER API
- `heal_awards_pubs.csv` - a table of publications associated with HEAL awards
- `projects_not_in_reporter.txt` - a list of project numbers that do not return information from the NIH RePORTER API
- `projects_with_missing_nums.txt` - a list of project titles that do not contain project numbers and thus are not queryable with the NIH RePORTER API

## Updates

### 17 DEC 2021
This repository has been updated to now abstract out the `input file` (and corresponding `project_id` and `project_title` column names), `output path`, `output prefix` for the files.
The script is executed using the 

## Inputs

The list of HEAL projects was downloaded from the [funding awarded website](https://heal.nih.gov/funding/awarded).
Information about the API we use in this project can be found at the [NIH RePORTER API website](https://api.reporter.nih.gov/).

## Considerations

- The input data we work with here (namely, the list of HEAL projects) was last updated in March 2020.
- Some of the project numbers from the input data CSV are blank, meaning we can't get information from the NIH RePORTER API.
- Some project numbers are valid, but do not appear to be in NIH RePORTER.
- There does not seem to be a hook within the NIH Reporter wherein we could look up HEAL studies, thus we rely on the aforementioned input list.

## Quick Start
### Requirements

- Python 3.6+
- pip
- git
- venv
- bash

### Setup

- Clone the repository `git clone https://github.com/jcheadle-rti/heal_segmentation.git`
- Create and activate the virtual environment `python3 -m venv venv`
- Update pip and install required packages
  - `pip install --upgrade pip`
  - `pip install -r requirements.txt`
  
### Run Bash Script

- Review the bash script (`query_nih_reporter.sh`) to confirm the parameters are accurate
- At the command prompt, run `bash query_nih_reporter.sh`

## Outputs

- `heal_awards.csv` - a table of the HEAL awards and associated information from the NIH RePORTER API
- `heal_awards_pubs.csv` - a table of publications associated with HEAL awards
- `projects_not_in_reporter.txt` - a list of project numbers that do not return information from the NIH RePORTER API
- `projects_with_missing_nums.txt` - a list of project titles that do not contain project numbers and thus are not queryable with the NIH RePORTER API
