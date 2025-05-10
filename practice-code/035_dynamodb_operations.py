# pip install boto3

import boto3


# create a dynamodb client
dynamodb = boto3.resource('dynamodb')

# create a new table
table = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {
            'AttributeName': 'UserId',
            'KeyType': 'HASH'  # partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'UserId',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table created:", table.table_name)