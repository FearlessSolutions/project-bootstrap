import os
import boto3
import re

# Will launch an EC2
def launch_ec2(name):
  with open('resources/ec2-cloudformation.json', 'r') as myfile:
    cloudformation_template=myfile.read()#.replace('\n', '')
  stack_name = "DevOps-AutoCreate-"+re.sub("[^0-9a-zA-Z]","-",name)
  client = boto3.client(
    'cloudformation',
    region_name='us-east-1',
    aws_access_key_id=os.environ.get('AWS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET')
  )
  response = client.create_stack(
    StackName='DevOps-Autocreate-'+name,
    TemplateBody=cloudformation_template,
    Parameters=[
      {
        'ParameterKey': 'KeyName',
        'ParameterValue': 'charles-ec2',
        'UsePreviousValue': True
      },{
        'ParameterKey': 'InstanceType',
        'ParameterValue': 'm1.small',
        'UsePreviousValue': True
      },{
        'ParameterKey': 'SSHLocation',
        'ParameterValue': '0.0.0.0/0',
        'UsePreviousValue': True
      },{
        'ParameterKey': 'InstanceAvailabilityZone',
        'ParameterValue': 'us-east-1a',
        'UsePreviousValue': True
      },
    ],
    TimeoutInMinutes=30,
    OnFailure='ROLLBACK',
    Tags=[
      {
        'Key': 'BusinessUnit',
        'Value': 'devops-bootstrap'
      },
    ]
  )


