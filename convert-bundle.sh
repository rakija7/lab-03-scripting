#!/bin/bash
set -euo pipefail

curl -o lab3-bundle.tar.gz https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
tar -xzf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > lab3_data.csv

LINES=$(wc -l < lab3_data.csv | tr -d ' ')
COUNT=$((LINES-2))
echo "This CSV has "$COUNT" rows/lines."
tar -czvf converted-archive.tar.gz lab3_data.csv

