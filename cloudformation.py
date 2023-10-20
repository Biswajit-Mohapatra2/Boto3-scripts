# Verify if AWS CloudFormation stacks have notification configurations set.


import boto3

# Initialize a Boto3 client for CloudFormation
cloudformation = boto3.client('cloudformation')

# Get a list of all CloudFormation stacks
response = cloudformation.describe_stacks()

# Initialize an empty dictionary to store stack notification configuration information
stacks_notification_dict = {}

# Iterate through the CloudFormation stacks
for stack in response['Stacks']:
    stack_name = stack['StackName']

    # Describe the stack's notification configuration
    try:
        notification_config = cloudformation.describe_stack_resource(
            StackName=stack_name,
            LogicalResourceId='MyTopic',  # Change 'MyTopic' to the logical resource ID of your notification
        )
        
        # Check if notification configuration exists
        notification_exists = 'StackResourceDetail' in notification_config
        
        stack_info = {
            'Stack Status': stack['StackStatus'],
            'Notification Configuration Exists': notification_exists
        }

        stacks_notification_dict[stack_name] = stack_info
    except Exception as e:
        # Handle the case where the stack resource or topic does not exist
        stack_info = {
            'Stack Status': stack['StackStatus'],
            'Notification Configuration Exists': False
        }

        stacks_notification_dict[stack_name] = stack_info

# Print or return the dictionary with stack notification configuration information
print(stacks_notification_dict)
