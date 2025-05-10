# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'

EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource
VPC_ID       = 'vpc-xxxxxxxxxxxxx' # set the vpc id

security_group  = EC2_RESOURCE.create_security_group(
    Description = 'Allow inbound SSH traffic',
    GroupName   = 'allow-inbound-ssh',
    VpcId = VPC_ID,
    TagSecifications = [
        {
            'ResourceType': 'security-group',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'allow-inbound-ssh',
                },
            ]
        },
    ],
)
security_group.authorize_ingress(
    CidrIp = '0.0.0.0/0',
    FromPort = 22,
    ToPort = 22,
    IpProtocol = 'tcp',
)

print(f'Security Group {security_group.id} has been created')