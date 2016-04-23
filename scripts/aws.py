import os
import boto3
import re

# Will launch an EC2
def launch_ec2(name){
    stack_name = "DevOps-AutoCreate-"+re.sub("[^0-9a-zA-Z]","-",name)
    client = boto3.client(
	'cloudformation',
	aws_access_key_id=os.environ.get('AWS_KEY'),
	aws_secret_access_key=environ.get('AWS_SECRET')
    }
    response = client.create_stack(
	StackName='DevOps-Autocreate-'+name,
	TemplateBody='string',
	TemplateURL='string',
	Parameters=[
	    {
		'ParameterKey': 'string',
		'ParameterValue': 'string',
		'UsePreviousValue': True|False
	    },
	],
	DisableRollback=True|False,
	TimeoutInMinutes=123,
	NotificationARNs=[
	    'string',
	],
	Capabilities=[
	    'CAPABILITY_IAM',
	],
	ResourceTypes=[
	    'string',
	],
	OnFailure='DO_NOTHING'|'ROLLBACK'|'DELETE',
	StackPolicyBody='string',
	StackPolicyURL='string',
	Tags=[
	    {
		'Key': 'string',
		'Value': 'string'
	    },
	]
    )
}


