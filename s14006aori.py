import ghActivity
import sys
import os
from datetime import datetime
from boto.ses.connection import SESConnection

os.environ['TZ'] = 'UTC'

gh = ghActivity.ghActivity()
feed = gh.getFeedById('s14006')
latest = {}

for entry in feed:
  if entry['title'].find('s14006/31day') >= 0:
    latest = entry
    break

if latest: 
  if (datetime.now() - datetime.strptime(latest['updated'],'%Y-%m-%dT%H:%M:%SZ')).days:
    message = '今日コミットした?'
    conn = SESConnection()
    conn.send_email(sys.argv[1],'ghActivityTest',message,[sys.argv[1]]) 
