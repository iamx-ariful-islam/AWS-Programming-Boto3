# pip install boto3

import boto3


# set the region
AWS_REGION  = 'ap-north-2'
# set bucket
SRC_BUCKET  = 'Axsa-src-bucket'
DST_BUCKET  = 'Axsa-dst-bucket'
S3_RESOURCE = boto3.resource('s3', region_name=AWS_REGION) # s3 resource

# copy object function
def copy_objects():
    src_bucket = S3_RESOURCE.Bucket(SRC_BUCKET)
    dst_bucket = S3_RESOURCE.Bucket(DST_BUCKET)
    print(f'Source S3 bucket: {SRC_BUCKET}')
    print(f'Destination S3 bucket: {DST_BUCKET}')
    
    for s3_object in src_bucket.objects.all():
        print(f'Copying object: {s3_object.key}')
        source_file_data = {
            'Bucket': SRC_BUCKET,
            'Key': s3_object.key,
        }
        dst_bucket.copy(source_file_data, s3_object.key)
    print('Copy done')
    
copy_objects()