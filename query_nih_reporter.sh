#!/bin/bash
set -e

# Specify base directory
FULL_PATH=$(realpath $0)
OUTPUT_BASE=$(dirname $FULL_PATH)
echo "Base Directory: " $OUTPUT_BASE

# Specify Run directory - **EDIT HERE**
RUN_DATE="22_DEC_2021"
mkdir $OUTPUT_BASE/outputs/$RUN_DATE

# Generate files from NIH RePORTER - **EDIT HERE**
python3 heal_award_segmenter.py $OUTPUT_BASE/inputs/awarded_08_DEC_2021.csv $OUTPUT_BASE/outputs/$RUN_DATE $RUN_DATE --project-id-column "proj_num" --project-title-column "proj_tittle"