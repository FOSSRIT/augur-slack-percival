-- Creating the 'slack_user' table
CREATE TABLE slack_user (
    user_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    real_name VARCHAR(255),
    display_name VARCHAR(255),
    team_id VARCHAR(255),
    is_admin BOOLEAN,
    is_owner BOOLEAN,
    is_primary_owner BOOLEAN,
    is_restricted BOOLEAN,
    is_ultra_restricted BOOLEAN,
    is_bot BOOLEAN,
    updated TIMESTAMP WITH TIME ZONE,
    profile_image_url TEXT
    -- Add other user fields here as necessary
);

-- Creating the 'slack_message' table
CREATE TABLE slack_message (
    message_id SERIAL PRIMARY KEY,
    type VARCHAR(50),
    user_id VARCHAR(255) REFERENCES slack_user(user_id),
    text TEXT,
    ts TIMESTAMP WITH TIME ZONE,
    team VARCHAR(255),
    client_msg_id VARCHAR(255),
    channel_id VARCHAR(255),
    -- Add other message fields here as necessary
    FOREIGN KEY (channel_id) REFERENCES slack_channel(channel_id)
);

-- Creating the 'slack_channel' table
CREATE TABLE slack_channel (
    channel_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    created TIMESTAMP WITH TIME ZONE,
    is_channel BOOLEAN,
    is_group BOOLEAN,
    is_im BOOLEAN,
    is_archived BOOLEAN,
    is_general BOOLEAN,
    unlinked SMALLINT,
    name_normalized VARCHAR(255),
    is_shared BOOLEAN,
    is_org_shared BOOLEAN,
    is_pending_ext_shared BOOLEAN,
    creator_id VARCHAR(255),
    is_read_only BOOLEAN,
    is_thread_only BOOLEAN,
    is_non_threadable BOOLEAN,
    num_members INT
    -- Can add other channel fields here as necessary
);

-- adding indexes on frequently searched columns for faster queries
CREATE INDEX idx_slack_message_user_id ON slack_message(user_id);
CREATE INDEX idx_slack_message_channel_id ON slack_message(channel_id);
CREATE INDEX idx_slack_user_team_id ON slack_user(team_id);
CREATE INDEX idx_slack_channel_name ON slack_channel(name);
