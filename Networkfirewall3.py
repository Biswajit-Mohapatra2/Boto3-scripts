import boto3

# Initialize a Boto3 client for Network Firewall
network_firewall = boto3.client('network-firewall')

# List all Network Firewall policies
response = network_firewall.list_policies()

# Initialize a dictionary to store policies and their associated rule groups
policy_rule_groups = {}

# Iterate through the policies
for policy in response['PolicyList']:
    policy_name = policy['PolicyName']
    
    # Describe the policy to get its associated rule groups
    policy_info = network_firewall.describe_policy(PolicyName=policy_name)

    rule_group_associations = policy_info['Policy']['RuleGroupReferences']

    # Extract the rule group names from the associations
    rule_group_names = [assoc['ResourceName'] for assoc in rule_group_associations]

    policy_rule_groups[policy_name] = rule_group_names

# Print or return the dictionary with policies and their associated rule groups
for policy_name, rule_groups in policy_rule_groups.items():
    print(f"Policy Name: {policy_name}")
    print(f"Associated Rule Groups: {', '.join(rule_groups)}")
    print()
