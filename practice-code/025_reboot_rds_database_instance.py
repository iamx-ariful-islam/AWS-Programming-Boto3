# pip install boto3

import boto3


# create rds client
client   = boto3.client('rds')

response = client.reboot_db_instance(
    DBInstanceIdentifier = 'database-instance-01'
)
print(response)