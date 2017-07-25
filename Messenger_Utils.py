"""############################################################################
Utility functions for handling messenges
############################################################################"""
import sys

#Importing module for fb chatting
sys.path.append('./package')
import fbchat
import fbchat.models as mod


# =============================================================================
# Function to check whether a message is sent by a certain individual
#
# Input:
#   - user_id: the uid of the individual I want to check
#   - message: the fbchat.models.Message object I am checking
#
# Output:
#   True / False depending on whether the message was sent my the user_id
# =============================================================================
def is_message_author(user_id, message):
    if ( str(message.author) == str(user_id) ):
        return True
    else:
        return False


# =============================================================================
# Function to find the first sublist of consecutive messages
#   * Since the list is most recent --> oldest order, this should get the most
#     recent consecutive messages
#
# Input:
#   - user_id: the uid of the individual I want to get the message for
#   - message_list: a list of fbchat.models.Message objects
#
# Output:
#   A sublist of fbchat.models.Message objects, containing the first appearance
#   of a message sent by user_id, and subsequent consecutive messages
# =============================================================================
def get_consec_messages(user_id, message_list):
    #Find the first appearance of message sent by this individual
    m_idx = 0
    while m_idx < len(message_list):
        #If the current index belongs to the indv, break loop to advance
        if is_message_author(user_id, message_list[m_idx]):
            break
        #If not, keep advancing the start index
        m_idx += 1

    #Check if we have exausted the messages
    if m_idx >= len(message_list):
        return []

    #Else, initialize a message list
    message_sublist = [ message_list[m_idx] ]
    #Get consecutive messages by the same individual
    m_idx += 1
    while m_idx < len(message_list) and is_message_author(user_id, message_list[m_idx]):
        message_sublist.append(message_list[m_idx])
        m_idx += 1

    #Return the sublist
    return message_sublist
