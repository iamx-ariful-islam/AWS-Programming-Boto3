# pip install boto3

import boto3


# create an ec2 resource object
ec2 = boto3.resource('ec2')

# launch an ec2 instance
instance = ec2.create_instances(
    ImageId='ami-xxxxxxxxxxxxxxxxx',  # replace with a valid ami id
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
)

print("EC2 instance created with ID:", instance[0].id)