# heal_segmentation

This repository holds scripts, input data, and output data relevant to the HEAL award segmentation task for the NIH HEAL effort.  

## Updates
Cleaned input data waas added on **11 NOV 2021**; new outputs appended with "_05_NOV_2021".
Manually transformed IDs are shown in `inputs/corrected_project_ids_11_NOV_2021.csv`

New input data was added on **05 NOV 2021**; new outputs appended with "_05_NOV_2021".

## Inputs

The list of HEAL projects was downloaded from the [funding awarded website](https://heal.nih.gov/funding/awarded).
Information about the API we use in this project can be found at the [NIH RePORTER API website](https://api.reporter.nih.gov/).

## Considerations

- The input data we work with here (namely, the list of HEAL projects) was last updated in March 2020.
- Some of the project numbers from the input data CSV are blank, meaning we can't get information from the NIH RePORTER API.  See list [here](/outputs/projects_with_missing_nums.txt).
- Some project numbers are valid, but do not appear to be in NIH RePORTER.  See list [here](/outputs/projects_not_in_reporter.txt).
- There does not seem to be a hook within the NIH Reporter wherein we could look up HEAL studies, thus we rely on the aforementioned input list.

## Quick Start
### Requirements

- Python 3.6+
- pip
- git
- venv

### Setup

- Clone the repository `git clone https://github.com/jcheadle-rti/heal_segmentation.git`
- Create and activate the virtual environment `python3 -m venv venv`
- Update pip and install required packages
  - `pip install --upgrade pip`
  - `pip install -r requirements.txt`
  
### Run Script

- At the command propmt, run `python3 heal_award_segmenter.py`

## Outputs

- `heal_awards.csv` - a table of the HEAL awards and associated information from the NIH RePORTER API
- `heal_awards_pubs.csv` - a table of publications associated with HEAL awards
- `projects_not_in_reporter.txt` - a list of project numbers that do not return information from the NIH RePORTER API
- `projects_with_missing_nums.txt` - a list of project titles that do not contain project numbers and thus are not queryable with the NIH RePORTER API
