import boto3

# Initialize a Boto3 client for EC2
ec2 = boto3.client('ec2')

ssh_filter = [
    {
        'Name': 'ip-permission.to-port',
        'Values': ['22']
    },
    {
        'Name': 'ip-permission.from-port',
        'Values': ['22']
    }
]

response = ec2.describe_security_groups(Filters=ssh_filter)

security_groups_dict = {}

for group in response['SecurityGroups']:
    group_info = {
        'Group Name': group['GroupName'],
        'Description': group.get('Description', 'N/A'),
        'Inbound SSH Rules': []
    }

    for permission in group['IpPermissions']:
        if permission['FromPort'] == 22 and permission['ToPort'] == 22:
            for ip_range in permission.get('IpRanges', []):
                group_info['Inbound SSH Rules'].append(ip_range['CidrIp'])

    security_groups_dict[group['GroupId']] = group_info

print(security_groups_dict)
