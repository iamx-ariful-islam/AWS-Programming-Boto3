# pip install boto3

import boto3


# set the region
AWS_REGION   = 'ap-north-2'
ec2_resource = boto3.resource('ec2', region_name=AWS_REGION) # ec2 resource

for volume in ec2_resource.volumes.filter(Filters=[{'Name':'status', 'Values':['available']}]):
    if volume.state == 'available':
        volume_id = volume.id
        volume.delete()
        print(f'Volume {volume_id} successfully deleted')
    else:
        print("Can't delete volume attached to EC2 instance")