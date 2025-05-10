# pip install boto3

import boto3


# create an s3 client
s3 = boto3.client('s3')

# create a new s3 bucket
bucket_name = "my-new-bucket-12345"
s3.create_bucket(Bucket=bucket_name)

# upload a file to the bucket
s3.upload_file('local_file.txt', bucket_name, 'uploaded_file.txt')

print(f"File uploaded to {bucket_name}")