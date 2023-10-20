# Retrieve the supported EKS cluster versions.


import boto3

# Initialize a Boto3 client for EKS
eks = boto3.client('eks')

# Get a list of supported EKS cluster versions
response = eks.list_cluster_versions()

# Extract the supported versions from the response
supported_versions = response.get('versions', [])

# Print or return the list of supported EKS cluster versions
print("Supported EKS Cluster Versions:")
for version in supported_versions:
    print(version)
