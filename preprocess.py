import re
import pandas as pd
import datetime


def process(data):
    data2 = data[159:]

    messages = {}

    # Iterate through the lines in the conversation
    for line in data2.splitlines():

        # Split the line into its components
        parts = line.split(" - ")
    #     print(parts)
        # Get the date and time of the message
        timestamp = datetime.datetime.strptime(parts[0], "%m/%d/%y, %I:%M %p")

        # Get the sender and recipient of the message
        sender, recipient = parts[1].split(": ")

        # Get the message text
        message = parts[1].split(": ")[1]
    #     print(parts)
    #     print(parts[2])
        # Add the message to the dictionary
        messages[timestamp] = {
            "sender": sender,
            "recipient": recipient,
            "message": message,
        }

    timestamps = []
    mes = []
    for timestamp, message in messages.items():
        timestamps.append(timestamp)
        mes.append(message['message'])
        # print(timestamp,message['message'])
        
        
    df = pd.DataFrame()
    df['time'] = timestamps
    df['message'] = mes

    user = []
    for i,m in messages.items():
        user.append(m['sender'])

    df['user'] = user
    # df = df[df!='<Media omitted>']

    df2 = df.dropna()
    df3= df2.reset_index(drop=True)
    df3['year'] = df3['time'].dt.year
    df3['month'] = df3['time'].dt.month_name()
    df3['day'] = df3['time'].dt.day
    df3['minute'] = df3['time'].dt.minute
    
    return df3
