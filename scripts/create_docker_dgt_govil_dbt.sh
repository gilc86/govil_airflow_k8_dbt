echo "create docker for dgt_govil_dbt"
echo "creator: Gil Kal"

cd /home/gilc/projects/govil_airflow_k8_dbt/

# Check the $DIRECTORY is exists
DIRECTORY_REPO = 'govil_airflow_k8_dbt'
if [ -d "$DIRECTORY_REPO" ]; then
  echo "$DIRECTORY_REPO does exist."
  rm -rf $DIRECTORY_REPO
fi

