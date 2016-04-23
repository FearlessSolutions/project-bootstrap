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

print "Let's get started!"

project_name = "devops-"+''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(7))
project_name = raw_input( "First, give a name for your project, or hit [enter] for default name ["+project_name+"]: ") or project_name
project_name = re.sub("[^0-9a-zA-Z]","-",project_name)

create_slack = confirm("1) Should I create a SLACK channel with title '"+project_name+"'?")
create_github = confirm("2) Should I create a GITHUB repository with name '"+project_name+"'?")
create_aws = confirm("3) Should I create an EC2 instance named '"+project_name+"'?")

print "Received project name: "+project_name

response = "Here are the results:\n"
if create_slack:
  print "# Creating slack channel '"+project_name+"'"
  #response += slack.create_channel(project_name) + "\n"
else:
  print "NOT creating slack channel."

if create_github:
  print "# Creating GitHub repository"
  response += fearless_github.create_repo(project_name) + "\n"
else:
  print "NOT creating github repo."

if create_aws:
  print "# Creating EC2 instance"
  #response += aws.launch_ec2(project_name) + "\n"
else:
  print "NOT creating EC2 instance."

print "\n\n### Completed all integrations."
print response
