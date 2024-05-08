# Slack Data Access with Sir Perceval

This project automates the process of adding a Slack bot to all channels, extracting messages, and storing them in a PostgreSQL database using Perceval and custom Python scripts.

## Prerequisites

1. **Python**: Make sure Python is installed on your machine.
2. **psycopg2**: Install the psycopg2 library to interact with PostgreSQL.
pip install psycopg2
3. **Sir Perceval**: Install Perceval to collect data from Slack.
4. **Slack Bot**: Create a bot for the specific Slack workspace and obtain the API token.

## Files Included

- `PercevalDatabaseQueries.sql`: SQL scripts to create the necessary database tables.
- `AddBotToChannels.py`: Script to add the Slack bot to all channels.
- `PercevalDatabaseImplementation.py`: Implements the data extraction from Slack and inserts data into the database.
- `PercevalTest.py`: Test script to verify the data extraction.

## Setup and Execution

### Step 1: Database Setup

1. Run the SQL code from `PercevalDatabaseQueries.sql` to create all necessary tables in your PostgreSQL database.

### Step 2: Add Bot to Channels

1. Execute `AddBotToChannels.py` to automatically add your Slack bot to all channels and collect channel IDs.

### Step 3: Data Ingestion

1. Run `PercevalDatabaseImplementation.py` to collect messages and related relevant data.Further, store it in the tables created earlier in your database.
python PercevalDatabaseImplementation.py


## Configuration

Ensure to replace the place-holders in all the scripts with actual database credentials, API token.

