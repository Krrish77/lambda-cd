import json

def lambda_handler(event, context):
    # TODO implement
    
    print("Execution started")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from top gun')
    }
