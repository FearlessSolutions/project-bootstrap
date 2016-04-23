#!/usr/bin/env python
import settings

from scripts import fearless_github
from scripts import slack
from scripts import ec2

project_name = "devops-autocreate-3"

print "Calling github script..."
#fearless_github.create_repo(project_name)
print "Done github!"

print "Creating slack channel..."
#slack.create_channel(project_name)
print "Done slack!"

print "Creating EC2..."
#
print "Done ec2!"
