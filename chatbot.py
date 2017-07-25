"""############################################################################
Main chat script
############################################################################"""

#Importing typical modules
import sys
from getpass import getpass

#Importing module for fb chatting
sys.path.append('./package')
import fbchat
import fbchat.models as mod


# =============================================================================
# Get my password and login
# =============================================================================
# Getting my password!
with open('vault/fb_pass.txt', 'r') as pass_file:
    password = pass_file.read().strip()
#Login to fb
username = 'anthony.chen.100'
client = fbchat.Client(username, password)


#NOTE: testing below


print "Getting users"
users = client.fetchAllUsers()
for user in users:
    if 'clever' in user.name or 'Clever' in user.name:
        print user.name


#Send somet stuff to cleverbot
usr_id = 'CleverBot' #TODO: add actual user id
message_toUsr = 'test'
client.sendMessage(message_toUsr, thread_id=usr_id, thread_type=mod.ThreadType.USER)

#NOTE: testling above

# =============================================================================
# Begin chatbot loop
# =============================================================================
#while True:
    #Get the last 6 messages from the thread
    #Process the message to form a single string
    #Send to chatbot api and receive response
    #If response time is reached - respond


#Send myself a message
#client.sendMessage('Hi me!', thread_id=client.uid, thread_type=fbchat.models.ThreadType.USER)

#mes = client.fetchThreadMessages(thread_id=client.uid, limit=5)

#for m in mes:
#    print m.text

#mod.MessageReaction('SMILE')


client.logout()
sys.exit()
