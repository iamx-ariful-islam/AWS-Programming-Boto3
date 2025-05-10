# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'

EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource
EC2_CLIENT   = boto3.client('ec2', region_name=AWS_REGION) # create ec2 client
volume       = EC2_RESOURCE.Volume('vol-xxxxxxxxxxxxx') # set ec2 volume

print(f'Volume {volume.id} status -> {volume.state}')

volume.detach_from_instance(
    Device = '/dev/sdb',
    InstanceId = 'i-xxxxxxxxxxxxx',
)

waiter = EC2_CLIENT.get_waiter('volume available')
waiter.wait(
    VolumeIds = [
        volume.id,
    ]
)

print(f'Volume {volume.id} status -> {volume.state}')