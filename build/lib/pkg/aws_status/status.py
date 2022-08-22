from optparse import Values
import sys
import boto3
import logging
import pkg.utils.client.client as client
import pkg.utils.common.common as common
from botocore.exceptions import ClientError
import time
# import config

# AWS_AZ class is checking the status of Ec2 instances


class AWS_AZ():
    def __init__(self, client=None):
        self.clients = client

    # CheckAWSStatus will verify and give the ec2 instance details
    def CheckAWSStatus(self, experimentsDetails):

        self.clients = client.AWSClient().clientEC2
        if experimentsDetails.InstanceTag == "" or experimentsDetails.InstanceRegion == "":
            return ValueError("Provided EC2InstanceTag or InstanceRegion are empty")
        
        try:
            filters = [{'Name':'tag:instanceSchedule', 'Values': ['*Webserver*']}]

            instances = self.clients.instances.filter(Filters=filters)

            # For each insteance with a tag
            for i in instances:
                for tag in i.tags:
                    if tag['Key'] == 'Name':
                        instanceName = tag['Value']
                        print(instanceName)
                        experimentsDetails.EC2InstanceTag = instanceName
        except ClientError as e:
            logging.error(e.args[0])
            print(e)
            




        

from optparse import Values
import sys
import boto3
import logging
import pkg.utils.client.client as client
import pkg.utils.common.common as common
from botocore.exceptions import ClientError
import time
# import config

# AWS_AZ class is checking the status of Ec2 instances


class AWS_AZ():
    def __init__(self, client=None):
        self.clients = client

    # CheckAWSStatus will verify and give the ec2 instance details
    def CheckAWSStatus(self, experimentsDetails):

        self.clients = client.AWSClient().clientEC2
        if experimentsDetails.InstanceTag == "" or experimentsDetails.InstanceRegion == "":
            return ValueError("Provided EC2InstanceTag or InstanceRegion are empty")
        
        try:
            filters = [{'Name':'tag:instanceSchedule', 'Values': ['*Webserver*']}]

            instances = self.clients.instances.filter(Filters=filters)

            # For each insteance with a tag
            for i in instances:
                for tag in i.tags:
                    if tag['Key'] == 'Name':
                        instanceName = tag['Value']
                        print(instanceName)
                        experimentsDetails.EC2InstanceTag = instanceName
        except ClientError as e:
            logging.error(e.args[0])
            print(e)
            




        

