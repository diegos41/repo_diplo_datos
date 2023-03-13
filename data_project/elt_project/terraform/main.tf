
#DO NOT INCLUDE .JSON FILE WITH CREDENTIALS IN THE GITHUB REPO.

terraform {
    required_version = ">= 1.0"
    backend "local" {} #In production, you'd use cloud services ('gcs' for google, 's3' for aws, etc.) 
    required_providers {
        google ={
            source = "hashicorp/google" 
        }
    } #this declaration is optional. It's like importing a library and then using the predefined functions in 'resources'.

}

provider "google" {
    project = var.project
    region = var.region
    #credentials = file(var.credentials) It's used when you don't want to set GOOGLE-APPLICATION_CREDENTIALS.

}

#Data Lake Bucket
#Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket
resource "google_storage_bucket" "data_lake_bucket" {
  name = "${local.data_lake_bucket}_${var.project}" #Concatenating DL bucket & project name for unique naming
  location = var.region
#See ref for more optional settings
}

#BigQuery Dataset
#Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset
resource "google_bigquery_dataset" "dataset" {
    dataset_id = var.BQ_DATASET
    project = var.project
    location = var.region 
}