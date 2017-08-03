"""############################################################################
Main chat script

Note:
    - Currently just setting up a chat loop with a single user
############################################################################"""

#Importing typical modules
import sys
import time
from getpass import getpass

#Importing module for fb chatting
sys.path.append('./package')
import fbchat
import fbchat.models as mod

#Importing my own modules (should be in same directory)
import Messenger_Utils as MU

# =============================================================================
# Setting up variables
# =============================================================================
#Chat ID for CleverBot
CLEVERBOT_ID = '228305623846705'
#Chat ID for the individual I wish to talk to
INDV_ID = '000000000000000' #TODO: put friend's ID here

# =============================================================================
# Get my password from file, log in to my fb messenger
# =============================================================================
# Getting my password!
with open('vault/fb_pass.txt', 'r') as pass_file:
    password = pass_file.read().strip()
#Login to fb
username = 'anthony.chen.100'
client = fbchat.Client(username, password)


# =============================================================================
# Begin chatbot loop
# =============================================================================
user_id = INDV_ID #Active person that I talk to
bot_id = CLEVERBOT_ID #Bot replying on my behalf

while True: #TODO some condition here
    #Get the last 6 messages from the thread
    user_mes_list = client.fetchThreadMessages(thread_id=user_id, limit=6)
    #Check I didn't send the last message
    while MU.is_message_author(client.uid, user_mes_list[0]):
        time.sleep(10) #TODO: temp solution
        user_mes_list = client.fetchThreadMessages(thread_id=user_id, limit=6)

    #Get the sublist of the received message
    received_m = MU.get_consec_messages(user_id, user_mes_list)
    #Join together the list in reversed order to form a string
    received_str = ' '.join(m.text for m in reversed(received_m))

    print received_str

    #Send this off to cleverbot to get its reply
    client.sendMessage(received_str, thread_id=bot_id, thread_type=mod.ThreadType.USER)

    #Wait for clever bot to reply
    bot_mes_list = client.fetchThreadMessages(thread_id=bot_id, limit=3)
    while MU.is_message_author(client.uid, bot_mes_list[0]):
        time.sleep(2) #TODO: temp solution
        bot_mes_list = client.fetchThreadMessages(thread_id=bot_id, limit=3)

    #Get the bots reply
    bot_mes = MU.get_consec_messages(bot_id, bot_mes_list)
    bot_mes_str = ' '.join(m.text for m in reversed(bot_mes))

    print bot_mes_str
    #Send the bot's message to the user
    client.sendMessage(bot_mes_str, thread_id=user_id, thread_type=mod.ThreadType.USER)

client.logout()
