# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'

EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource
volume       = EC2_RESOURCE.Volume('vol-xxxxxxxxxxxx') # ec2 volume

if volume.state == 'available':
    volume.delete()
    print(f'Volume successfully deleted')
else:
    print(f'Can\'t delete volume attached to EC2 instance')