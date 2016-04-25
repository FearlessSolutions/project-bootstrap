import os
import inspect
from slacker import Slacker

# Creates a slack channel

def create_channel(name):
  slack = Slacker(os.environ.get("SLACK_TOKEN"))

  # Create channel
  slack.channels.create(name)
  channels = slack.channels.list()

  # Get some test users to add
  users = []
  for user in slack.users.list().body['members']:
    if (user['name'] == "delali") or (user['name'] == "charles"):
      users.append(user['id'])

  # Add users to appropriate channel.  Not necessary if channel was successfully created, but i wanted to dick around
  for channel in channels.body['channels']:
    if channel['name'] == name:
      for user in users:
        slack.channels.invite(channel['id'], user)
  return "Successfully created slack channel "+name
