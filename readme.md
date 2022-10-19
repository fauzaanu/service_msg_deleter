# Delete Service Messages Bot
Simple and straight-forward implementation of a Telegram Bot that deletes services messages that are added by telegram.
Telegram should make this a feature at this point.

- Works on a single chat
  - why? : When public bots are made to erase all service messages one public bot owner gets access to all the messages of the chat
  - This is a privacy risk
  - Also a lot of the public bots slow down occasionally because they cannot handle it
  - instead one bot can definitely handle one chat
  - And the group owner can have his own delete bot so the data doesn't leak
- `THE_GROUPS_CHAT_ID is the chatid of the group`
- To get the chatid just uncomment the only print statement
  - `# print(update)`
  - Send any message in the chat and you should get an update
  - The chatid will be the first id you find within the chat object
  - Or use a bot such as @MyChatInfoBot

# INSTALLATION + RUNNING

### Windows
1. clone this repo or download as zip
2. edit the windows.bat file with your full locations
   - The first path (python) described the main program you are using to run the script
   - The second one is the script.py
   - In other words you are using python.exe to run pythonscript.py
3. Note that python.exe is inside the venv/scripts folder so you dont need to install it
4. Launch the .bat file to make sure it runs.
5. When it succesfully runs remove the pause and add the .bat file into windows task sheduler
6. In windows task sheduler when you add the action there are some optional params
   - The start in parameter is absolutely nessesary
   - Pass it the folder where the .bat file is located at
   - Best to make the bot start with windows or anyhow you like
     - Bot will not stop itself unless you manually stop

### Ubuntu Server
- clone
- start the vitual env
- if creating new venv
  - pip install python-telegram-bot --pre
- run python3 main.py