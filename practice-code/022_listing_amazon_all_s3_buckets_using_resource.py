# pip install boto3

import boto3


# set the region
AWS_REGION = 'ap-north-2'

resource   = boto3.resource('s3', region_name=AWS_REGION) # s3 resource
iterator   = resource.buckets.all() # get s3 buckets

print('Listing Amazon S3 Buckets')
for bucket in iterator:
    print(f"{bucket.name}")