# Verify if AWS Redshift clusters are using the default database name.


import boto3

# Initialize a Boto3 client for Redshift
redshift = boto3.client('redshift')

# Get a list of all Redshift clusters
response = redshift.describe_clusters()

# Initialize an empty dictionary to store Redshift cluster information
redshift_clusters_dict = {}

# Define the default database name to check against
default_db_name = 'dev'

# Iterate through the Redshift clusters
for cluster in response['Clusters']:
    cluster_id = cluster['ClusterIdentifier']
    cluster_info = {
        'Cluster Status': cluster['ClusterStatus'],
        'Using Default Database Name': cluster['DBName'].lower() == default_db_name.lower()
    }

    redshift_clusters_dict[cluster_id] = cluster_info

# Print or return the dictionary with Redshift cluster information
print(redshift_clusters_dict)
