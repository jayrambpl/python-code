import json

def lambda_handler(event, context):
    # Parse and print the incoming event
    print("Received event: " + json.dumps(event, indent=2))

    # Your business logic goes here

    return {
        'statusCode': 200,
        'body': json.dumps('Event processed successfully')
    }

