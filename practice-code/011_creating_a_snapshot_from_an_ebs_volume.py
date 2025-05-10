# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'

EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource
VOLUME_ID    = 'vol-xxxxxxxxxxxxx' # set volume id

snapshot =  EC2_RESOURCE.create_snapshot(
    VolumeId = VOLUME_ID,
    TagSpecifications = [
        {
            'ResourceType': 'snapshot',
            'Value': [
                {
                    'Key': 'Name',
                    'Value': 'Axsa-ebs-snapshot',
                },
            ]
        },
    ]
)

print(f'Snapshot {snapshot.id} created for volume {VOLUME_ID}')