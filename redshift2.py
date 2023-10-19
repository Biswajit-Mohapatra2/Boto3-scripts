import boto3

# Initialize a Boto3 client for Redshift
redshift = boto3.client('redshift')

# Get a list of all Redshift clusters
response = redshift.describe_clusters()

redshift_clusters_dict = {}

# Define the default admin username to check against
default_admin_username = 'admin'

# Iterate through the Redshift clusters
for cluster in response['Clusters']:
    cluster_id = cluster['ClusterIdentifier']
    cluster_info = {
        'Cluster Status': cluster['ClusterStatus'],
        'Using Default Admin Account': cluster['MasterUsername'].lower() == default_admin_username.lower()
    }

    redshift_clusters_dict[cluster_id] = cluster_info

# Print or return the dictionary with Redshift cluster information
print(redshift_clusters_dict)
