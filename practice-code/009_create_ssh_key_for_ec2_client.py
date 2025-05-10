# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource

key_pair    = EC2_RESOURCE.create_key_pair(
    KeyName = 'Axsa-ssh-key-pair',
    TagSpecifications = [
        {
            'ResourceType': 'key-pair',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Axsa-ssh-key-pair'
                },
            ]
        },
    ]
)

print(f'SSH key fingerprint: {key_pair.key_fingerprint}')
print(f'Private SSH key: {key_pair.key_material}')