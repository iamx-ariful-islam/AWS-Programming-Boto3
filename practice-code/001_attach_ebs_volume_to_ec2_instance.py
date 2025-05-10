# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource
volume       = ec2_resource.Volume('vol-xxxxxxxxxxxxxx') # resource volume

print(f'Volume {volume.id} status -> {volume.state}')

volume.attach_to_instance(
    Device = '/dev/sdb',
    InstanceId = 'i-xxxxxxxxxxxxxxxxx',
)

print(f'Volume {volume.id} status -> {volume.state}')