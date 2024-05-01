import boto3
lambda_client = boto3.client('lambda')

def clean_lambda_space(function_name, versions_to_keep):
    # function_name = 'pulse-dev-profile' #add your Lambda Function Name here
    # versions_to_keep = 10 #Number of version to keep
    
    response = lambda_client.list_versions_by_function(
        FunctionName=function_name
    )
    versions = response['Versions']
    versions.sort(key=lambda v: v['Version'])
    total_versions = len(versions)
    versions_to_delete = total_versions - versions_to_keep
    for version in versions:
        if version['Version'] == '$LATEST': #Skip the latest version
            continue
        versions_to_delete-=1
        if versions_to_delete <= 0: #break if all version deleted
            break 
        version_number = version['Version']
        lambda_client.delete_function(
            FunctionName=function_name,
            Qualifier=version_number
        )
    return True

function_name_to_delete  = "pulse-qa-profile"
versions_to_keep = 10
clean_lambda_space(function_name_to_delete,versions_to_keep )


