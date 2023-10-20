# Confirm if AWS CodeDeploy Lambda deployments have disabled "All at Once" traffic shifting.


import boto3

# Initialize a Boto3 client for CodeDeploy
codedeploy = boto3.client('codedeploy')

# Get a list of all deployments
response = codedeploy.list_deployments()

# Initialize an empty dictionary to store deployment information
deployment_dict = {}

# Iterate through the deployments
for deployment_id in response['deployments']:
    deployment_info = codedeploy.get_deployment(
        deploymentId=deployment_id
    )

    deployment_group_name = deployment_info['deploymentInfo']['deploymentGroupName']
    traffic_config = deployment_info['deploymentInfo'].get('trafficRoutingConfig', {})
    is_all_at_once_disabled = traffic_config.get('timeBasedCanary', {}).get('isEnabled', True) and \
        traffic_config.get('timeBasedLinear', {}).get('isEnabled', True)

    deployment_dict[deployment_id] = {
        'Deployment Group Name': deployment_group_name,
        'All at Once Disabled': is_all_at_once_disabled
    }

# Print or return the dictionary with deployment information
print(deployment_dict)
