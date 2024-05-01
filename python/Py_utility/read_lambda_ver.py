import boto3
import os
from datetime import datetime

aws_access_key = 'AKIA2NNUTTKA5RQH5P6X'
aws_secret_key = '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'
aws_region = 'us-east-1'

def list_lambda_versions(client, function_name):

    first_ver = ''
    last_ver = ''
    Desc = ''

    try:
        response = client.list_versions_by_function(FunctionName=function_name)
        versions = response['Versions']
        if versions:
            first_version = versions[0]
            first_ver = first_version['Version']
            Desc = first_version['Description']
            if len(versions) > 1:
                last_version = versions[-1]
                last_ver = last_version['Version']
                Desc = last_version['Description']
                last_modified_str = last_version.get('LastModified')
                if last_modified_str:
                    last_modified_datetime = datetime.strptime(last_modified_str, '%Y-%m-%dT%H:%M:%S.%f+0000')
                    formatted_last_modified = last_modified_datetime.strftime('%Y-%m-%d %H:%M:%S')

    except Exception as e:
        print(f"Error: {e}")

    return formatted_last_modified, last_ver, Desc

# ------------------

def print_lambda_functions_by_prefix(lambda_client, prefix):

    try:
        functions = []
        next_marker = None

        while True:
            # Use the Marker parameter to paginate through results
            if next_marker:
                response = lambda_client.list_functions(Marker=next_marker)
            else:
                response = lambda_client.list_functions()

            current_page_functions = response['Functions']
            functions.extend(current_page_functions)

            # Check if there are more pages
            if 'NextMarker' in response:
                next_marker = response['NextMarker']
            else:
                break

        filtered_functions = [function for function in functions if function['FunctionName'].startswith(prefix)]

        for function in filtered_functions:
            formatted_last_modified, last_ver, Desc = list_lambda_versions(lambda_client, function['FunctionName'])
            print(f"{function['FunctionName'].ljust(35)} {Desc.ljust(45)} Ver: {last_ver.ljust(4)} {formatted_last_modified}")
            # print(f"Function Name: {function['FunctionName']}, ARN: {function['FunctionArn']}")
            
            
    except Exception as e:
        print(f"Error: {e}")
    # -------
    # for function_info in response['Functions']:
    #     if function_info['FunctionName'].startswith(prefix):
    #         last_modified_str = function_info.get('LastModified')
            
    #         if last_modified_str:
            
    #             last_modified_datetime = datetime.strptime(last_modified_str, '%Y-%m-%dT%H:%M:%S.%f+0000')
    #             formatted_last_modified = last_modified_datetime.strftime('%Y-%m-%d %H:%M:%S')
    #         else:
    #             formatted_last_modified = "Not available"    

    #         first_ver, last_ver, Desc = list_lambda_versions(lambda_client, function_info['FunctionName'])
    #         last_ver = last_ver.ljust(4)
            
    #         print(f"{function_info['FunctionName'].ljust(35)} {function_info['Description'].ljust(45)} Ver:{last_ver} {formatted_last_modified} ")
    #         # print(f"First Version: {first_ver} Last Version: {last_ver} Description: {Desc}")
    #         # print("\n")

# --------------------


# ---------------
def main():
    # Create Lambda client
    lambda_client = boto3.client('lambda', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    # Print information about Lambda functions with a specific prefix
    prefix_to_search = 'pulse-dev'
    print_lambda_functions_by_prefix(lambda_client, prefix_to_search)

if __name__ == "__main__":
    main()






