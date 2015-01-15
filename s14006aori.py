import ghActivity
from datetime import datetime
import boto

gh = ghActivity.ghActivity()
feed = gh.getFeedById('s14006')
latest = {}

for entry in feed:
  if entry['title'].find('s14006/31day') >= 0:
    latest = entry
    break

if latest: 
  print(latest) 
