import requests
import pandas as pd

def join_all_public_channels(token):
        # URLs for Slack API to list and join channels
    list_url = 'https://slack.com/api/conversations.list'
    join_url = 'https://slack.com/api/conversations.join'
    channels_df = pd.DataFrame(columns = ['channel_id'])
    headers = {'Authorization': f'Bearer {token}'}

    # Parameters for the API call to list public channels, excluding the archived channels
    params = {
        'limit': 200,
        'types': 'public_channel',
        'exclude_archived': 'true'
    }
    
   
    channels_to_join = []
    
    # Looping through all public channels using pagination
    while True:
        response = requests.get(list_url, headers=headers, params=params).json()
        if not response['ok']:
            raise Exception(f"Error listing channels: {response['error']}")


        # Adding channel IDs to the list
        channels = response['channels']
        for channel in channels:
            channels_to_join.append(channel['id'])
        
        #Handling Paginatino
        next_cursor = response['response_metadata']['next_cursor']
        if not next_cursor:
            break
        params['cursor'] = next_cursor
    
    # Joining each channel and logging the result (can be removed for production code)
    for channel_id in channels_to_join:
        join_response = requests.post(join_url, headers=headers, json={'channel': channel_id}).json()
        if not join_response['ok']:
            print(f"Error joining channel {channel_id}: {join_response['error']}")
        else:
            print(f"Joined channel: {channel_id}")
            channels_df = channels_df.append({'channel_id':channel_id},ignore_index = True)

    channels_df.to_csv('channel_ids.csv',index = False)# saving the channel ids to a csv. TODO: add backend integration to add these channel ids to the Workspace table.

# Slack API Token / A bot for each workspace has to be created to access data
slack_api_token = ''  

join_all_public_channels(slack_api_token)
