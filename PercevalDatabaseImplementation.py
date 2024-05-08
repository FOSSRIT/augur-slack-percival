from perceval.backends.core.slack import Slack
import json
import pandas as pd
import psycopg2



def insert_data_from_json_list(json_data, db_config):
    # Connecting to the PostgreSQL database
    conn = psycopg2.connect(
        host=db_config['host'],
        database=db_config['database'],
        user=db_config['user'],
        password=db_config['password']
    )
    cur = conn.cursor()


    # Iterating through each entry in the JSON data list
    for mylist in json_data:
        user = mylist['data']['user_data']
        message = mylist['data']
        channel = mylist['data']['channel_info']
        print(channel['name'])


        # Inserting channel data
        cur.execute("""
            INSERT INTO slack_channel (channel_id, name, created, is_channel, num_members)
            VALUES (%s, %s, to_timestamp(%s), %s, %s) ON CONFLICT (channel_id) DO NOTHING;
            """,
            (channel['id'], channel['name'], float(channel['created']), channel['is_channel'], channel['num_members'])
        )

        # Inserting user data
        cur.execute("""
            INSERT INTO slack_user (user_id, name, real_name, is_admin, is_bot)
            VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING;
            """,
            (user['id'], user['name'], user['real_name'], user['is_admin'], user['is_bot'])
        )

        # Inserting message data
        cur.execute("""
            INSERT INTO slack_message (message_id, user_id, channel_id, text, ts)
            VALUES (%s, %s, %s, %s, to_timestamp(%s)) ON CONFLICT (message_id) DO NOTHING;
            """,
            (message['ts'], user['id'], channel['id'], message['text'], float(message['ts']))
        )

    # Commiting the changes
    conn.commit()
    # closing connection
    cur.close()
    conn.close()

# Database configuration
db_config = {
    'host': 'localhost',
    'database': 'database_name',
    'user': 'username',
    'password': 'password'
}


slack_api_token = '' # add slack api token
channels_df = pd.read_csv('channel_ids.csv') # add the path to you csv file with the channel ids OR TODO: add backed integration for the Workspace Table which has channel ids.

# Using Sir Perceval to get slack data and Inserting to our data base. 
for channel_id in channels_df['channel_id']:
    
    slack = Slack(api_token=slack_api_token,channel=channel_id)#workspace=workspace,

    messages_list = []
    for message in slack.fetch(category="message"):
        # Process and store messages
        messages_list.append(message)
    insert_data_from_json_list(messages_list, db_config)
# save_file = 'messages.json'

# with open(save_file,'w',encoding ='utf-8') as f :
#     json.dump(messages_list,f,ensure_ascii = False ,indent = 4) 
# all_messages_df.to_csv('final_data_normalized.csv',index = False)
