from perceval.backends.core.slack import Slack
import json
import pandas as pd
# from grimoirelab.perceval.backends.chat.slack import Slack

# from grimoirelab.perceval.backends.chat.slack import Slack


slack_api_token = ''


channels_df = pd.read_csv('channel_ids.csv') # add the path to you csv file with the channel ids.

all_messages_df = pd.DataFrame()



for channel_id in channels_df['channel_id']:
    
    slack = Slack(api_token=slack_api_token,channel=channel_id)#workspace=workspace,

    # messages_list = []
    for message in slack.fetch(category="message"):
        # Process and store messages
        # messages_list.append(message) # Use if a json file needs to be created
        # print(message)
        # all_messages_df = all_messages_df.append(pd.Series(message),ignore_index = True) Use if message data is needed in a stream. 
        message_data = pd.json_normalize(message) 
        # Appending the message data to the all_messages_df DataFrame
        all_messages_df = pd.concat([all_messages_df, message_data], ignore_index=True)

all_messages_df.to_csv('final_data_normalized.csv',index = False)

# save_file = 'messages.json'
# with open(save_file,'w',encoding ='utf-8') as f :
#     json.dump(messages_list,f,ensure_ascii = False ,indent = 4) 
