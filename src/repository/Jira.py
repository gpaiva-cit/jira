from config import config
from jira import JIRA

jira = JIRA(
    server = config.JIRA_SERVER,
    token_auth = config.JIRA_TOKEN
)
