# Check if AWS CodeDeploy deployments have a minimum number of healthy hosts configured for Amazon EC2 instances.


import boto3

# Initialize a Boto3 client for CodeDeploy
codedeploy = boto3.client('codedeploy')

# Get a list of all deployments
response = codedeploy.list_deployments()

# Initialize an empty dictionary to store deployment information
deployment_dict = {}

# Minimum number of healthy hosts required (modify as needed)
minimum_healthy_hosts = 2

# Iterate through the deployments
for deployment_id in response['deployments']:
    deployment_info = codedeploy.get_deployment(
        deploymentId=deployment_id
    )

    # Check if a minimum number of healthy hosts is configured
    deployment_group_info = deployment_info['deploymentInfo']['loadBalancerInfo']['targetGroupPairInfo'][0]
    is_minimum_healthy_hosts_configured = (
        deployment_group_info['trafficRoute']['listenerArns'][0]['listener']['defaultActions'][0].get('fixed', 0) >= minimum_healthy_hosts
    )

    deployment_dict[deployment_id] = {
        'Deployment Group Name': deployment_info['deploymentInfo']['deploymentGroupName'],
        'Minimum Healthy Hosts Configured': is_minimum_healthy_hosts_configured
    }

# Print or return the dictionary with deployment information
print(deployment_dict)
