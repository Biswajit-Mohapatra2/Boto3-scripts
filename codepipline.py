# Verify if AWS CodePipeline deployments meet the specified deployment count criteria.


import boto3

# Initialize a Boto3 client for CodePipeline
codepipeline = boto3.client('codepipeline')

# Specify the pipeline name you want to check
pipeline_name = 'YourPipelineName'

# Specify the deployment count criteria
desired_deployments = 5

# Get pipeline state
response = codepipeline.get_pipeline_state(name=pipeline_name)

# Initialize an empty dictionary to store pipeline deployment information
pipeline_deployments = {}

# Iterate through the stages of the pipeline
for stage in response['stageStates']:
    stage_name = stage['stageName']
    
    # Check if the stage has deployments and meets the specified criteria
    if 'latestExecution' in stage:
        deployment_count = stage['latestExecution'].get('summary', '').count('Deploy')
        meets_criteria = deployment_count == desired_deployments
    else:
        deployment_count = 0
        meets_criteria = False

    stage_info = {
        'Deployment Count': deployment_count,
        'Meets Criteria': meets_criteria
    }

    pipeline_deployments[stage_name] = stage_info

# Print or return the dictionary with pipeline deployment information
print(pipeline_deployments)
