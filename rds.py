import boto3

# Initialize a Boto3 client for RDS
rds = boto3.client('rds')

# Get a list of all RDS instances
response = rds.describe_db_instances()

# Initialize an empty dictionary to store RDS instance information
rds_instances_dict = {}

# Iterate through the RDS instances
for instance in response['DBInstances']:
    instance_id = instance['DBInstanceIdentifier']
    instance_info = {
        'DB Engine': instance['Engine'],
        'Master Username': instance['MasterUsername'],
        'Default Admin Account Used': instance['MasterUsername'].lower() == 'admin'
    }

    rds_instances_dict[instance_id] = instance_info

# Print or return the dictionary with RDS instance information
print(rds_instances_dict)
