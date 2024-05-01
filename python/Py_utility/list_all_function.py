import boto3

def list_all_lambda_functions():
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    aws_access_key = 'XXX'
    aws_secret_key = 'XXX'
    aws_region = 'us-east-1'


    client = boto3.client('lambda', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

    try:
        functions = []
        next_marker = None

        while True:
            # Use the Marker parameter to paginate through results
            if next_marker:
                response = client.list_functions(Marker=next_marker)
            else:
                response = client.list_functions()

            current_page_functions = response['Functions']
            functions.extend(current_page_functions)

            # Check if there are more pages
            if 'NextMarker' in response:
                next_marker = response['NextMarker']
            else:
                break

        for function in functions:
            print(f"Function Name: {function['FunctionName']}, ARN: {function['FunctionArn']}")
    
    except Exception as e:
        print(f"Error: {e}")

# Replace 'your_function_name' with the name of your Lambda function
list_all_lambda_functions()
