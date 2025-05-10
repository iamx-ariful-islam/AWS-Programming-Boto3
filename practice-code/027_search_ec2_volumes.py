# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'
ec2_resource = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource

for volume in ec2_resource.volumes.filter(
    Filters = [
        {
            'Name': 'tag:Name',
            'Values': [
                'Axsa-Code',
                ]
            }
        ]
    ):
    print(f'Volume {volume.id} ({volume.size}GiB) - {volume.state}')