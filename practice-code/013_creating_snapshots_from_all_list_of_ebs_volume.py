# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'

EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource
snapshots    = EC2_RESOURCE.snapshots.all() # get the screenshots

for snapshot in snapshots:
    print(f'Snapshot {snapshot.id} created for volume {snapshot.volume.id}')