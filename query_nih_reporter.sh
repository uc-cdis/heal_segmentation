#!/bin/bash
set -e

# Specify base directory
FULL_PATH=$(realpath $0)
OUTPUT_BASE=$(dirname $FULL_PATH)
echo "Base Directory: " $OUTPUT_BASE

# Specify Run directory - **EDIT HERE**
# RUN_DATE="03_FEB_2022"
mkdir -p $OUTPUT_BASE/outputs

# Generate files from NIH RePORTER appl_ids
python3 heal_award_segmenter.py "appl_id" $OUTPUT_BASE/inputs/HEAL_FY1821.csv $OUTPUT_BASE/outputs/ "with_mds_dump" --input_awarded_filepath $OUTPUT_BASE/inputs/awarded.csv --input_mds_dump_filepath $OUTPUT_BASE/inputs/preprod-healdata-org-discovery_metadata.tsv --gen3_field_mapping_filepath $OUTPUT_BASE/inputs/field_mappings.json --project-id-column "Appl ID" --project-title-column "Title" --replace-non-utf  --add-gen3-authz-value
# python3 heal_award_segmenter.py "appl_id" $OUTPUT_BASE/inputs/HEAL_FY1821_short.csv $OUTPUT_BASE/outputs/ "short_with_mds_dump" --input_awarded_filepath $OUTPUT_BASE/inputs/awarded.csv --input_mds_dump_filepath $OUTPUT_BASE/inputs/preprod-healdata-org-discovery_metadata.tsv --gen3_field_mapping_filepath $OUTPUT_BASE/inputs/field_mappings.json --project-id-column "Appl ID" --project-title-column "Title" --replace-non-utf  --add-gen3-authz-value

# Generate files from NIH RePORTER project_nums
#python3 heal_award_segmenter.py "project_num" $OUTPUT_BASE/inputs/HEAL_FY1821.csv $OUTPUT_BASE/outputs/$RUN_DATE $RUN_DATE --project-id-column "Full Grant Number" --project-title-column "Title" --replace-non-utf
