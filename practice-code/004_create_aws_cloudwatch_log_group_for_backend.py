# pip install boto3

import json
import boto3


# set the region
AWS_REGION = 'ap-north-2'
CLIENT     = boto3.client('logs', region_name=AWS_REGION) # create logs client

retention_period_in_days = 5

# backend and log group
log_group = 'CRMBackendLogs'
response  = CLIENT.create_log_group(
    LogGroupName = log_group,
    tags = {
        'Type': 'Back end',
        'Frequency': '30 seconds',
        'Environment': 'Production',
        'RetentionPeriod': str(retention_period_in_days)
    }
)

print(json.dumps(response, indent=4))

response = CLIENT.put_retention_policy(
    LogGroupName = log_group,
    retensionInDays = retention_period_in_days
)

print(json.dumps(response, indent=4))