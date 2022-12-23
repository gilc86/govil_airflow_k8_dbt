#!/bin/bash
echo "create docker for dgt_govil_dbt"
echo "creator: Gil Kal"

cd /home/gilc/projects/

# Check the $DIRECTORY_REPO is exists
DIRECTORY_REPO = 'govil_airflow_k8_dbt'
if [ -d "$DIRECTORY_REPO" ]; then
  echo "$DIRECTORY_REPO does exist."
  rm -rf $DIRECTORY_REPO
  echo "$DIRECTORY_REPO as deleted."
fi

git clone https://github.com/gilc86/govil_airflow_k8_dbt.git

