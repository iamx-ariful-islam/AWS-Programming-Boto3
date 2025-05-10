# pip install boto3

import boto3


# set the region
AWS_REGION  = 'ap-north-2'

client      = boto3.client('s3', region_name=AWS_REGION) # create s3 client
BUCKET_NAME = 'Axsa-bucket' # set bucket name

location = {'LocationConstraint': AWS_REGION}
response = client.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration=location)

print(f'Amazon {BUCKET_NAME} S3 bucket has been created')