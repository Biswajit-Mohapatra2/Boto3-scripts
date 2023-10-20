# Check for AWS S3 bucket policies that grant permissions to specific grantee types.


import boto3
import json

# Initialize a Boto3 client for S3
s3 = boto3.client('s3')

# Specify the name of your S3 bucket
bucket_name = 'your-bucket-name'

# Specify the grantee type you want to check (e.g., 'CanonicalUser' or 'AmazonCustomerByEmail')
target_grantee_type = 'CanonicalUser'

# Get the bucket policy
response = s3.get_bucket_policy(Bucket=bucket_name)

# Initialize a flag to track if the grantee type is found
grantee_type_found = False

# Parse the bucket policy
bucket_policy = json.loads(response['Policy'])

# Check for the grantee type in the bucket policy
for statement in bucket_policy.get('Statement', []):
    if 'Principal' in statement:
        principal = statement['Principal']
        if isinstance(principal, dict):
            for key in principal:
                if target_grantee_type in key:
                    grantee_type_found = True
                    break

# Print or return the result indicating if the grantee type is found
if grantee_type_found:
    print(f"The bucket policy of {bucket_name} grants permissions to {target_grantee_type}.")
else:
    print(f"The bucket policy of {bucket_name} does not grant permissions to {target_grantee_type}.")
