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

    # Check if automatic rollback monitoring is enabled for this deployment
    is_auto_rollback_enabled = deployment_info['deploymentInfo'].get('autoRollbackConfiguration', {}).get('enabled', False)

    deployment_dict[deployment_id] = {
        'Deployment Group Name': deployment_info['deploymentInfo']['targetInstances'][0]['deploymentId'],
        'Auto Rollback Enabled': is_auto_rollback_enabled
    }

# Print or return the dictionary with deployment information
print(deployment_dict)
