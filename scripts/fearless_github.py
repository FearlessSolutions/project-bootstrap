import os
import inspect
from github import Github

# Creates github repo
def create_repo(name):
  print "Connecting to API"
  g = Github(os.environ.get("GITHUB_API_USER"), os.environ.get("GITHUB_API_TOKEN"))
  org = g.get_organization(os.environ.get("GITHUB_ORGANIZATION"))
  print "Creating GitHub repository..."
  #TODO: Uncomment this
  repo = org.create_repo(name)
  print "Done."

  print "Adding repository to devops team..."
  team = org.get_team(int(os.environ.get("GITHUB_TEAM")))
  print team.name
  print team.id
  team.add_to_repos(repo)
  print "Done."
