locals {
    data_lake_bucket = "dtc_data_lake"
    #These are the equivalent to constants.
}

#Variables are passed at runtime. The ones with "default" are optional whereas the ones without it are mandatory.

variable "project" {
    description = "Your GCP Project ID"
}

variable "region" {
    description = "Region for GCP resources. Choose as per your lcoation: https://cloud.google.com/about/locations"
    default = "southamerica-east1" #São-Paulo is the closest and most complete.
    type = string
}

#Other optional variables... (See Video 1.3.2)

variable "BQ_DATASET" {
    description = "BigQuery Dataset that raw data (from GCS) will be written into"
    type = string
    default = "trips_data_all"
}

#this is not a resource in main.tf yet
variable "TABLE_NAME" {
    description = "BigQuery table"
    type = string
    default = "ny_trips"
}
