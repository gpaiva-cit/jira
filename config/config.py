import os
from dotenv import load_dotenv

load_dotenv()

JIRA_SERVER = 'https://jiracloud.cit.com.br/'
JIRA_TOKEN = os.getenv('JIRA_TOKEN')
