#!/usr/bin/env python
import settings
import string
import random
import re

from scripts import fearless_github
from scripts import slack
from scripts import aws

def confirm(message):
  confirmed = None
  while confirmed is None:
    response = (raw_input(message+" [Yn]: ").lower() or 'y')
    if response.startswith('y'): confirmed = True
    if response.startswith('n'): confirmed = False
  return confirmed

with open('resources/fearless.txt', 'r') as fearless:
  print fearless.read()

print "This application will assist you in bootstrapping an application."
project_name = "devops-"+''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(7))
project_name = raw_input( "Give a name for your project ["+project_name+"]: ") or project_name
project_name = re.sub("[^0-9a-zA-Z]","-",project_name)

create_slack = confirm("Create a slack channel with title '"+project_name+"'?")
create_github = confirm("Create a github repository with name '"+project_name+"'?")
create_aws = confirm("Create a dev EC2 instance name '"+project_name+"'?")

print "Received project name: "+project_name

if create_slack:
  print "Creating slack channel '"+project_name+"'..."
  #slack.create_channel(project_name)
  print "Successfully created slack channel!"
else:
  print "NOT creating slack channel."

if create_github:
  print "Calling github script..."
  #fearless_github.create_repo(project_name)
  print "Done github!"
else:
  print "NOT creating github repo."

if create_aws:
  print "Creating EC2..."
#aws.launch_ec2(project_name)
  print "Done ec2!"
else:
  print "NOT creating EC2 instance."
