# Benjie.me Slackbot Tutorial
# https://blog.benjie.me/building-a-slack-bot-to-talk-with-a-raspberry-pi/
# code: https://gist.github.com/benjiao/a86581472d4925f61a314f5dadf2345c
# slack_client = testbot

import re
import time
import json
import psutil
from slackclient import SlackClient

slack_client = SlackClient('xoxb-150809089365-384973292688-dbw7HU7CYLvxjjUO6ngYcLFL')

# Fetch your Bot's User ID
user_list = slack_client.api_call('users.list')
for user in user_list.get('members'):
  if user.get('name') == 'testbot':
    slack_user_id = user.get('id')
    break


# Start connection
if slack_client.rtm_connect():
  print "Connected!"
  
  while True:
    for message in slack_client.rtm_read():
      if 'text' in message and message['text'].startswith("<@%s>" % slack_user_id):
        print "Message received: %s" % json.dumps(message, indent=2)
        message_text = message['text'].\
          split("<@%s>" % slack_user_id)[1].\
          strip()
        
        if re.match(r'.*(cpu).*', message_text, re.IGNORECASE):
          cpu_pct = psutil.cpu_percent(interval=1, percpu=False)
          
          slack_client.api_call(
            "chat.postMessage",
            channel=message['channel'],
            text="My CPU is at %s%%." % cpu_pct,
            as_user=True)

        if re.match(r'.*(memory|ram).*', message_text, re.IGNORECASE):
          mem = psutil.virtual_memory()
          mem_pct = mem.percent

          slack_client.api_call(
            "chat.postMessage",
            channel=message['channel'],
            text="My RAM is at %s%%." % mem_pct,
            as_user=True)

  time.sleep(1)


