import boto3

# Initialize a Boto3 client for Network Firewall
network_firewall = boto3.client('network-firewall')

# List all stateless rule groups
response = network_firewall.list_rule_groups()

# Initialize a list to store non-empty stateless rule groups
non_empty_stateless_rule_groups = []

# Iterate through the rule groups
for rule_group in response['RuleGroups']:
    rule_group_name = rule_group['RuleGroupName']
    
    # Describe the rule group to get its rules
    rule_group_info = network_firewall.describe_rule_group(RuleGroupName=rule_group_name)

    # Check if the rule group has rules
    if 'Rules' in rule_group_info:
        non_empty_stateless_rule_groups.append(rule_group_name)

# Print or return the list of non-empty stateless rule groups
print("Non-Empty Stateless Rule Groups:")
for rule_group_name in non_empty_stateless_rule_groups:
    print(rule_group_name)
