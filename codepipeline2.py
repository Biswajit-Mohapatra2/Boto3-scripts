import boto3

# Initialize a Boto3 client for CodePipeline
codepipeline = boto3.client('codepipeline')

# Specify the pipeline name you want to check
pipeline_name = 'YourPipelineName'

# Get pipeline details
response = codepipeline.get_pipeline(name=pipeline_name)

# Initialize a flag to track whether a region fanout action is used
region_fanout_used = False

# Iterate through the stages of the pipeline
for stage in response['pipeline']['stages']:
    for action in stage.get('actions', []):
        if 'regionFanout' in action.get('actionTypeId', {}).get('category', ''):
            region_fanout_used = True
            break

# Print or return the result indicating if region fanout is used
if region_fanout_used:
    print(f"{pipeline_name} uses a region fanout action for cross-region deployments.")
else:
    print(f"{pipeline_name} does not use a region fanout action for cross-region deployments.")
