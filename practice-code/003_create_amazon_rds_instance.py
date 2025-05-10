# pip install boto3

import boto3


# create rds client
client   = boto3.client('rds')

# create client database
response = client.create_db_instance(
    AllocatedStorage = 5,
    DBInstanceClass = 'db.t2.micro',
    DBInstanceIdentifier = 'database-instance-01',
    Engine = 'MySQL',
    MasterUserPassword = 'password',
    MasterUsername = 'username',
)

print(response)