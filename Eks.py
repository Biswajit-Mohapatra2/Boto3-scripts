# Verify if secrets stored in Amazon EKS (Elastic Kubernetes Service) are encrypted.


import boto3

# Initialize a Boto3 client for KMS
kms = boto3.client('kms')

# Initialize a Boto3 client for EKS
eks = boto3.client('eks')

# Specify the name of your EKS cluster
cluster_name = 'YourEksClusterName'

# List the secrets for the specified EKS cluster
response = eks.list_secrets(clusterName=cluster_name)

# Initialize a list to store the results
encrypted_secrets = []

# Check the encryption status for each secret
for secret in response['secrets']:
    secret_name = secret['name']
    
    # Get the ARN of the KMS key used to encrypt the secret
    kms_key_arn = secret['kmsKeyArn']

    # Describe the KMS key to check if it's enabled (encrypted)
    try:
        kms_key_info = kms.describe_key(KeyId=kms_key_arn)

        if kms_key_info['KeyMetadata']['KeyState'] == 'Enabled':
            encrypted_secrets.append(secret_name)
    except Exception as e:
        pass

# Print or return the list of encrypted secrets
if encrypted_secrets:
    print("The following secrets are encrypted:")
    for secret in encrypted_secrets:
        print(secret)
else:
    print("No secrets found or all secrets are not encrypted.")
