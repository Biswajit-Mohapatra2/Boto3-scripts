# Retrieve all oldest supported EKS cluster versions.


import boto3

# Initialize a Boto3 client for EKS
eks = boto3.client('eks')

# List all available EKS clusters
clusters = eks.list_clusters()

# Initialize a dictionary to store the oldest supported versions
oldest_versions = {}

# Iterate through the EKS clusters
for cluster_name in clusters['clusters']:
    # Describe the cluster to get its version
    cluster_info = eks.describe_cluster(name=cluster_name)
    cluster_version = cluster_info['cluster']['version']

    if cluster_version not in oldest_versions:
        oldest_versions[cluster_version] = []

    oldest_versions[cluster_version].append(cluster_name)

# Print or return the dictionary with oldest supported versions
print("Oldest Supported EKS Cluster Versions:")
for version, clusters in oldest_versions.items():
    print(f"Version: {version}, Clusters: {', '.join(clusters)}")
