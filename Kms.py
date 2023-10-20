# Confirm if AWS Key Management Service (KMS) customer master keys (CMKs) have backing key rotation enabled.


import boto3

# Initialize a Boto3 client for KMS
kms = boto3.client('kms')

# Get a list of all CMKs
response = kms.list_keys()

# Initialize an empty dictionary to store CMK rotation information
cmk_rotation_dict = {}

# Iterate through the CMKs
for key in response['Keys']:
    cmk_id = key['KeyId']
    
    # Describe the key to check if key rotation is enabled
    key_info = kms.describe_key(KeyId=cmk_id)
    is_rotation_enabled = key_info['KeyMetadata']['KeyRotationEnabled']

    cmk_rotation_dict[cmk_id] = {
        'Key Name': key_info['KeyMetadata']['Description'],
        'Key Rotation Enabled': is_rotation_enabled
    }

# Print or return the dictionary with CMK rotation information
print(cmk_rotation_dict)
