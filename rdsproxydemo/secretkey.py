import json

import boto3
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "DEV_RDS_PROXY"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    client = boto3.client('secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        print(e)
        raise e

        # Your code goes here.

    # Decrypts secret using the associated KMS key.
    secret = json.loads(get_secret_value_response['SecretString'])
    print("secret :: {}".format(secret))

    return secret
