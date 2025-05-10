# pip install boto3

import boto3


# set the region
AWS_REGION = 'ap-north-2'

client     = boto3.client('s3', region_name=AWS_REGION) # create s3 client
response   = client.list_buckets()

print('Listing Amazon S3 Buckets')
for bucket in response['Buckets']:
    print(f"{bucket['Name']}")