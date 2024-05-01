import boto3

def list_lambda_versions(function_name):
    # Replace 'your_access_key', 'your_secret_key', and 'your_region' with your AWS credentials and region
    aws_access_key = 'AKIA2NNUTTKA5RQH5P6X'
    aws_secret_key = '9O5q0/alZxanQKlJ8xfNQUmODZ+sPAQZj3VFBApd'
    aws_region = 'us-east-1'

    client = boto3.client('lambda', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

    try:
        response = client.list_versions_by_function(FunctionName=function_name)
        # print(response)
        versions = response['Versions']
        print("\n")
        # print(versions)
        if versions:
            first_version = versions[0]
            print(f"version: {first_version['Version']}")
            print(f"Description: {first_version['Description']}")
            
            if len(versions) > 1:
                last_version = versions[-1]
                print(f"version: {last_version['Version']}")
                print(f"Description: {last_version['Description']}")

   
    except Exception as e:
        print(f"Error: {e}")

# Replace 'your_function_name' with the name of your Lambda function
list_lambda_versions('pulse-qa-identitymgmt')
