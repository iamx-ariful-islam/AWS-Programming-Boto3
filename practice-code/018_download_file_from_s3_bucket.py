# pip install boto3

import boto3


# set the region
AWS_REGION  = 'ap-north-2'
BUCKET_NAME = 'Axsa-Bucket' # set bucket name

s3_resource = boto3.resource('s3', region_name=AWS_REGION) # s3 resource
s3_object   = s3_resource.Object(BUCKET_NAME, 'text.txt')
s3_object.download_file('/Axsa/test.txt')

print('S# object download complete')