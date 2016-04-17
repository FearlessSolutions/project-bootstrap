#!/usr/bin/env python
import settings

from scripts import fearless_github

print "Imported GitHub"

print "Calling github script..."
fearless_github.create_repo("testing-automated-project-1")
print "Done calling!"
