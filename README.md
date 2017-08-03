# FB_Messenger_Bot
A bot for Facebook Messenger

Instead of manually accessing an external chatbot API to handle the chatting AI, I realized that I could just re-route the messages to the CleverBot chatbot in Facebok Messenger.


## How it works (currently)
- Set variables below before running script:
  - `CLEVERBOT_ID`: FB Messenger ID for a chatbot
  - `INDV_ID`: FB Messenger ID for an individual you wish to talk to
- The script takes the last received messages from that individual, concatenates the string together and sends it to *CleverBot*
- Then the script takes the reply from *CleverBot* and sends it to the individual you are talking to
- (Very unsophisticated for now) while loop forever for continuous lively non-robotic conversations :)
