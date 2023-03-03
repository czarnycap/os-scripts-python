#!/usr/bin/env python3
"""
Script works only if environment variables are configured:
Environment variables - AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
AWS CLI credentials file - The default location is ~/.aws/credentials.
IAM role for Amazon EC2 instances - If the code is running on an EC2
instance with an IAM role, boto3 can retrieve the credentials automatically
"""

import boto3

def check_ec2_states_all_regions():

  """ initialize ec2 client """
  ec2 = boto3.client('ec2')

  regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

  """ iterate over each region"""
  for region in regions:
      print("Instances in region", region)


      """ initialize the EC2 resources """
      ec2 = boto3.resource('ec2', region_name=region)

      """ get list of all instances in the region """
      instances = ec2.instances.all()

      """ print instances """
      for i in instances:
          print("Instance ID:", i.id)
          print('State:', i.state['Name'])

  return regions