import boto3

# Initialize a Boto3 client for Redshift
redshift = boto3.client('redshift')

# Get a list of all Redshift clusters
response = redshift.describe_clusters()

# Initialize an empty dictionary to store Redshift cluster audit logging information
redshift_clusters_dict = {}

# Iterate through the Redshift clusters
for cluster in response['Clusters']:
    cluster_id = cluster['ClusterIdentifier']
    cluster_info = {
        'Cluster Status': cluster['ClusterStatus'],
        'Audit Logging Enabled': cluster.get('ClusterAuditLoggingStatus', {}).get('AuditLoggingStatus', 'Not Enabled')
    }

    redshift_clusters_dict[cluster_id] = cluster_info

# Print or return the dictionary with Redshift cluster information
print(redshift_clusters_dict)
