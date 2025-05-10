# pip install boto3

import io
import boto3


# set the region
AWS_REGION     = 'ap-north-2'

S3_BUCKET_NAME = 'Axsa-Core' # set s3 bucket name
s3_resource    = boto3.resource('s3', region_name=AWS_REGION) # s3 resource
s3_object      = s3_resource.Object(S3_BUCKET_NAME, 'file_name.txt') # target file name

with io.BytesIO() as f:
    s3_object.download_fileobj(f)
    f.seek(0)
    print(f'This is the content of file:\n{f.read()}')