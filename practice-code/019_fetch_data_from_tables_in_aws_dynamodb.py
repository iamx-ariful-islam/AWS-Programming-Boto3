# pip install boto3

import boto3
from boto3.dynamodb.conditions import Key


# set the dynamodb database
dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('Employees') # set the database table name

response = table.query(KeyConditionExpression=Key('Name').eq('Michael'))

print('The query returned the following items:')
for item in response['Items']:
    print(item)