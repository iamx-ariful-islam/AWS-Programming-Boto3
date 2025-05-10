# pip install boto3

import time
import boto3


# set the region
AWS_REGION = 'ap-north-2'

EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION) # set EC2 client
VOLUME_ID  = 'vol-xxxxxxxxxxxx' # set volume id

def get_modification_state(volume_id):
    response = EC2_CLIENT.describe_volumes_modifications(
        VolumeIds = [
            volume_id
        ]
    )
    return response['VolumeModifications'][0]['ModificationState']

modify_volume_response = EC2_CLIENT.modify_volume(
    VolumeId = VOLUME_ID,
    Size = 30
)

while True:
    state = get_modification_state(VOLUME_ID)
    if state == 'completed' or state == None:
        break
    elif state == 'failed':
        raise Exception('Failed to modify volume size')
    else:
        time.sleep(60) # wait 1 mint
        
print(f'Volume {VOLUME_ID} successfully resized')