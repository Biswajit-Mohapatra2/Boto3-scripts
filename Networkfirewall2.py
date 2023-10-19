import boto3

# Initialize a Boto3 client for Network Firewall
network_firewall = boto3.client('network-firewall')

# Specify the default actions you want to filter by for stateless full packets
default_action_for_full_packets = 'ALERT'  # Change this to the desired default action

# List all Network Firewall policies
response = network_firewall.list_policies()

# Initialize a list to store policies with the specified default actions
policies_with_target_actions = []

# Iterate through the policies and filter by default actions for stateless full packets
for policy in response['PolicyList']:
    policy_name = policy['PolicyName']
    
    # Describe the policy to get its default actions
    policy_info = network_firewall.describe_policy(PolicyName=policy_name)

    # Check the default action for stateless full packets
    full_packets_default_action = policy_info['Policy']['StatelessDefaultActions']

    if full_packets_default_action == [default_action_for_full_packets]:
        policies_with_target_actions.append(policy_name)

# Print or return the list of policies with the specified default actions
print(f"Policies with Default Action for Stateless Full Packets: {', '.join(policies_with_target_actions)}")
