class RdsInstanceDefaultAdminCheck:
    def _init_(self, region="us-east-1", Account="", project_id=0):
        self.region = region
        self.account = Account
        self.project_id = project_id


    def list(self):
        # Create a Boto3 client for the Elastic Load Balancing (ELBv2) service
        elbv2_client = GetClient.get_client(service='elbv2', Account=self.account, project_id=self.project_id)

        # Get a list of all ALBs
        response = elbv2_client.describe_load_balancers()

        # Filter ALBs with WAF enabled
        albs_with_waf = [lb['LoadBalancerArn'] for lb in response['LoadBalancers'] if self.is_waf_enabled(lb['LoadBalancerArn'])]
        
        return albs_with_waf

    def is_waf_enabled(self, load_balancer_arn):
        # Create a Boto3 client for the AWS WAFv2 service
        wafv2_client = GetClient.get_client(service='wafv2', Account=self.account, project_id=self.project_id)

        # Get a list of all web ACLs (WAF ACLs)
        response = wafv2_client.list_web_acls(Scope='REGIONAL')

        # Check if any web ACL is associated with the specified ALB
        for web_acl in response['WebACLs']:
            if load_balancer_arn in web_acl['Scope']:
                return True

        return False