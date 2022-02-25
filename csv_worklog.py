import pandas as pd
from src.repository.worklog import add_worklog

# PATH_CSV = input("Address CSV file: ")
PATH_CSV = '.worklog/logging.csv'

logs = pd.read_csv(PATH_CSV)

for index, row in logs.iterrows():
    add_worklog(
        issue = row['issue'],
        comment = row['comment'],
        day = row['day'],
        time_started = row['time_started'],
        time_spent = row['time_spent']
    )
