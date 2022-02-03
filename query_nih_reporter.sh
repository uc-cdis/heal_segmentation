#!/bin/bash
set -e

# Specify base directory
FULL_PATH=$(realpath $0)
OUTPUT_BASE=$(dirname $FULL_PATH)
echo "Base Directory: " $OUTPUT_BASE

# Specify Run directory - **EDIT HERE**
RUN_DATE="03_FEB_2022"
mkdir $OUTPUT_BASE/outputs/$RUN_DATE

# Generate files from NIH RePORTER appl_ids
python3 heal_award_segmenter.py "appl_id" $OUTPUT_BASE/inputs/HEAL_FY1821.csv $OUTPUT_BASE/outputs/$RUN_DATE $RUN_DATE --project-id-column "Appl ID" --project-title-column "Title" --replace-non-utf

# Generate files from NIH RePORTER project_nums
# project here