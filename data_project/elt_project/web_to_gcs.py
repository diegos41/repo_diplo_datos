import os
import pandas as pd
import pyarrow
from google.cloud import storage
from pathlib import Path

"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

# services = ['fhv','green','yellow']
# switch out the bucketname
BUCKET = os.environ.get("GCP_GCS_BUCKET", "data_buket_name")


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def web_to_gcs(year, service):
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]       #this is for months >=10 (for example, in 010 you just need the last two digits)

        # csv file_name 
        file_name = f"{service}_tripdata_{year}-{month}"
    
        # read csv file and transform it into parquet
        request_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{service}/{file_name}.csv.gz"
        df = pd.read_csv(request_url)
        file_name = f"{file_name}.csv"

        #Added creation of the data/color directory:
        Path(f'data/{service}').mkdir(parents=True, exist_ok=True)

        path = Path(f'data/{service}/{file_name}').as_posix()

        df.to_csv(path, compression="gzip")
        print(f"CSV: {file_name}")

        # upload it to gcs 
        gcs_path= f"week4/{service}/{year}/{file_name}"
        upload_to_gcs(BUCKET, gcs_path, path)
        print(f"GCS: {gcs_path}")


####MAKE SURE YOU COMMENT THE DATASET YOU DON'T NEED TO UPLOAD

web_to_gcs('2019', 'green')
web_to_gcs('2020', 'green')
web_to_gcs('2019', 'yellow')
web_to_gcs('2020', 'yellow')
# web_to_gcs('2019', 'fhv')