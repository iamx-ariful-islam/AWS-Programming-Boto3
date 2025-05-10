# pip install boto3

import boto3
import pathlib


# find the base directory
BASE_DIR       = pathlib.Path(__file__).parent.resolve()

# set the region
AWS_REGION     = 'ap-north-2'

S3_BUCKET_NAME = 'axsa-code' # set the bucket name
s3_client      = boto3.client('s3', region_name=AWS_REGION) # create s3 client

# upload files by function calling
def upload_files(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client.upload_file(file_name, bucket, object_name)
    print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")

# call function by passing parameters
upload_files(f"{BASE_DIR}/Axsa/test.txt", S3_BUCKET_NAME)