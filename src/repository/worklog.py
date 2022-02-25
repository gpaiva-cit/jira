from src.helper.to_datetime import to_datetime
from src.repository.Jira import jira


def add_worklog(issue, comment, day, time_started, time_spent):
    jira.add_worklog(
        issue = issue,
        comment = comment,
        started = to_datetime(day, time_started),
        timeSpent = time_spent
    )
