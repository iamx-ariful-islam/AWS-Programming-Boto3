# pip install boto3

import boto3


# set the region
AWS_REGION        = 'ap-north-2'

# set service name
SERVICE_NAME      = 'ec2'
KEY_PAIR_NAME     = 'micheal_key_test'
AMI_ID            = 'ami-xxxxxxxxxxxxxxxxxx'
SUBNET_ID         = 'subnet-xxxxxxxxxxxx'
SECURITY_GROUP_ID = 'sg-xxxxxxxxxxxxxxxx'
INSTANCE_PROFILE  = 'EC2-Admin'
USER_DATA         = '''user data here'''

EC2_RESOURCE      = boto3.resource(service_name=SERVICE_NAME, region_name=AWS_REGION) # ec2 resource
EC2_CLIENT        = boto3.client(SERVICE_NAME, AWS_REGION) # create ec2 client

instances   = EC2_RESOURCE.create_instances(
    ImageId = AMI_ID,
    InstanceType = 't2.micro',
    KeyName  = 'Axsa-key',
    MinCount = 1,
    MaxCount = 1,
    KeyName  = KEY_PAIR_NAME,
    SecurityGroupIds = [SECURITY_GROUP_ID],
    SubnetId = SUBNET_ID,
    UserData = USER_DATA,
    TagSpecifications = [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'my-ec2-instance',
                },
            ]
        },
    ]
)
for instance in instances:
    print(f'EC2 instance "{instance.id}" has been launched')
    instance.wait_until_running()
    EC2_CLIENT.associate_iam_instance_profile(
        IamInstanceProfile = {'Name': INSTANCE_PROFILE},
        InstanceId = instance.id,
    )
    print(f'EC2 instance profile "{INSTANCE_PROFILE}" has been attached')
    print(f'EC2 instance "{instance.id}" has been started')