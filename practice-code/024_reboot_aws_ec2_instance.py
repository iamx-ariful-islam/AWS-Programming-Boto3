# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'

EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource
INSTANCE_ID  = 'i-xxxxxxxxxx' # set instance id
instance     = EC2_RESOURCE.Instance(INSTANCE_ID)

instance.reboot()
print(f'EC2 instance "{instance.id}" has been rebooted')