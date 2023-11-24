# Stupid webhook sender
this is just a little script that I made so I can easily annoy my friend into doing things by pinging him on discord every 10 or so minutes.<br><br>
To setup the script:
1. create a .env with the following values
   1. webhook 
      1. the link to your webhook, server settings -> Integrations -> webhooks
   2. content 
      1. whatever you want to add, I reccomend doing <@<kbd>userID</kbd>> to mention them for increased annoyance
2. add the following to your cron service
   1. <kbd>crontab -e</kbd> to open the file
   2. add <kbd>*/5 * * * * /usr/bin/python3 /home/username/path/to/file/bot.py</kbd> to the end of the file
   3. close your editor

you're all done!