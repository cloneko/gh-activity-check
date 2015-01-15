import ghActivity
import sys
from datetime import datetime
from boto.ses.connection import SESConnection


gh = ghActivity.ghActivity()
feed = gh.getFeedById('s14006')
latest = {}

for entry in feed:
  if entry['title'].find('s14006/31day') >= 0:
    latest = entry
    break

if latest: 
  conn = SESConnection()
  conn.send_email(sys.argv[1],'ghActivityTest',latest,[sys.argv[1]]) 
