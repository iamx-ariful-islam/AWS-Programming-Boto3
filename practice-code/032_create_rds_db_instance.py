# pip install boto3

import boto3


# create rds client
client   = boto3.client('rds')

response = client.create_db_instance(
    AllocatedStorage=4,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='database-instance-01',
    Engine='MySQL',
    MasterUserPassword='xxxxxx',
    MasterUsername='test',
)

print(response)