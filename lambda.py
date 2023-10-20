# Retrieve Lambda functions with specified runtimes.


import boto3

# Initialize a Boto3 client for Lambda
lambda_client = boto3.client('lambda')

# Specify the runtime(s) you want to filter by
target_runtimes = ['python3.9', 'nodejs14.x']

# List all Lambda functions
response = lambda_client.list_functions()

# Initialize a list to store Lambda functions with the specified runtimes
functions_with_target_runtimes = []

# Iterate through the Lambda functions and filter by runtime
for function in response['Functions']:
    function_name = function['FunctionName']
    function_runtime = function['Runtime']

    if function_runtime in target_runtimes:
        functions_with_target_runtimes.append({
            'FunctionName': function_name,
            'Runtime': function_runtime
        })

# Print or return the list of Lambda functions with the specified runtimes
for function_info in functions_with_target_runtimes:
    print(f"Function Name: {function_info['FunctionName']}, Runtime: {function_info['Runtime']}")
