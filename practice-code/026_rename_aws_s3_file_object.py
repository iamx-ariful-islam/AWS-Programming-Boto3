# pip install boto3

import boto3


# set the region
AWS_REGION     = 'ap-north-2'

S3_BUCKET_NAME = 'Axsa-Code' # set your s3 bucket name
s3_resouce     = boto3.resource('s3', region_name=AWS_REGION) # s3 resource

# rename file by function
def rename_s3_object(bucket_name, old_name, new_name):
    old_s3_object = s3_resouce.Object(bucket_name, old_name)
    new_s3_object = s3_resouce.Object(bucket_name, new_name)
    new_s3_object.copy_from(
        CopySource = f'{bucket_name}/{old_name}'
    )
    old_s3_object.delete()
    print(f'{bucket_name}/{old_name} -> {bucket_name}/{new_name}')
    
# call the function with parameters
rename_s3_object(S3_BUCKET_NAME, 'test.txt', 'new_test.txt')