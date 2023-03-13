## Setup 
Firstly, infrastructure needs to be built using *Terraform*. Make sure you already have a GCP account and a Service Account created in it. (Check ***terraform/*** for further details).

```shell
# If you created an environment variable with GCP credentials.
# Refresh service-account's auth-token for this session
gcloud auth application-default login

# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan -var="project=<your-gcp-project-id>"

# Create new infra
terraform apply -var="project=<your-gcp-project-id>"

# (OPTIONAL) Delete infra after your work, to avoid costs on any running services
terraform destroy
```
Then, execute the script `web_to_gcs.py` locally.

On *BigQuery*, create tables for each service type (yellow and green) that will be used as sources in dbt.

Clone the ***dbt_production/*** directory into your repo if you're using dbt Cloud or download it if you're running dbt locally. Once that's done, run `dbt build` in the CLI to build the project from scratch (includes models and all its dependencies).
Check auto-generated documentation in a web page (really cool feature from dbt).

Once the fact table `fact_trips` is created in *BQ*, use it as a source in *Looker Studio*. Finally, you can create some tiles for finding interesting insights. (See ***results_dashboard.pdf*** for checking the ones I've done)





