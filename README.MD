# Manutença do Jira via Python

## Setup

-   Dado que já está instalado o `virtualenv`

-   Rodar o script `local-setup.sh` para fazer a instalação das dependências

```bash
$ ./local-setup.sh
```

-   Gerar um token de acesso no Jira (https://jiracloud.cit.com.br/secure/ViewProfile.jspa?selectedTab=com.atlassian.pats.pats-plugin:jira-user-personal-access-tokens) e rodar o script abaixo

```bash
$ echo "JIRA_TOKEN = <TOKEN GERADO>" > .env
```

<br />

## Worklogs

<br />

### # Worklogs - App

Executar o script `app_worklog.py` e seguir as instruções no terminal

```bash
$ . venv/bin/activate

$ python3 app_worklog.py
```

<br />

### # Worklogs - CSV

Gerar o CSV `.worklog/logging.csv` com as seguintes colunas:

-   issue
-   comment
-   day
-   time_started
-   time_spent

Após isso, basta executar o script `csv_worklog.py`

```bash
$ . venv/bin/activate

$ python3 csv_worklog.py
```
