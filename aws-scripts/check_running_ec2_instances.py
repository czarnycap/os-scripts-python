#!/usr/bin/env python3
"""
Script works only if environment variables are configured:

Environment variables - AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
AWS CLI credentials file - The default location is ~/.aws/credentials.
IAM role for Amazon EC2 instances - If the code is running on an EC2
instance with an IAM role, boto3 can retrieve the credentials automatically

"""

import argparse
import boto3


# function showing all ec2 instances
def check_ec2_states_all_regions():
    # initialize ec2 client
    ec2 = boto3.client("ec2")

    regions = [region["RegionName"] for region in ec2.describe_regions()["Regions"]]

    # iterate over each region
    for region in regions:
        print("Instances in region", region)

        # initialize the EC2 resources
        ec2 = boto3.resource("ec2", region_name=region)

        # get list of all instances in the region
        instances = ec2.instances.all()

        # print instances
        for i in instances:
            print("Instance ID:", i.id)
            print("State:", i.state["Name"])

def s3_check():
    # using AWS S3
    s3 = boto3.resource('s3')
    
    for bucket in s3.buckets.all():
        print(bucket.name)

def check_nat_gateways():
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Retrieve information about all NAT gateways in the account
    nat_gateways = ec2.describe_nat_gateways()

    # Create an empty list to hold the IDs of all enabled NAT gateways
    enabled_nat_gateway_ids = []

    # Iterate over the NAT gateways and check if each one is enabled
    for nat_gateway in nat_gateways['NatGateways']:
        nat_gateway_id = nat_gateway['NatGatewayId']
        nat_gateway_state = nat_gateway['State']
        nat_gateway_subnet_id = nat_gateway['SubnetId']

        # Check if the NAT gateway is enabled
        if nat_gateway_state == 'available':
            print(f"NAT gateway {nat_gateway_id} in subnet {nat_gateway_subnet_id} is enabled.")
            enabled_nat_gateway_ids.append(nat_gateway_id)
        else:
            print(f"NAT gateway {nat_gateway_id} in subnet {nat_gateway_subnet_id} is not enabled.")

    return enabled_nat_gateway_ids


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Check AWS account services status")
    parser.add_argument("--ec2-instances", action="store_true", help="Check for EC2 instances across regions")
    parser.add_argument("--s3-list", action="store_true", help="Check for S3 buckets")
    parser.add_argument("--nat-gateways", action="store_true", help="Check for NAT gateways" )



    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if no arguments were provided
    if not any(vars(args).values()):
        parser.print_help()    

    # Parse args
    if args.ec2_instances:
        print("Running EC2 instances:")
        check_ec2_states_all_regions()
    elif args.s3_list:
        print("List of s3 buckets:" )
        s3_check()
    elif args.nat_gateways:
        print("Check for NAT gateways:" )
        check_nat_gateways()
                

if __name__ == "__main__":
    main()
