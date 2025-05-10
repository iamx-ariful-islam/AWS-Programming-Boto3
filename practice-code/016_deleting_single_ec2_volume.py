# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource
volume       = ec2_resource.Volume('vol-xxxxxxxxxxxx') # set ec2 volume

if volume.state == 'available':
    volume.delete()
    print('Volume successfully deleted')
else:
    print("Can't delete volume attached to EC2 instance")