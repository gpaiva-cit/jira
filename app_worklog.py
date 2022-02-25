import os
import re
from src.repository.worklog import add_worklog

def custom_input(message, validation = lambda x : True):
    try:
        print('\n')
        str_input = input(message)

        if str_input.lower() == ':quit':
            os._exit(0)

        if validation(str_input):
            return str_input
        else:
            print('Formato inválido')

    except KeyboardInterrupt:
        os._exit(0)

    except EOFError:
        os._exit(0)

    except:
        print('Formato inválido')

    return custom_input(message, validation)

project = custom_input("Project: ")

day = custom_input(
    "Day [dd/mm/yyyy]: ",
    lambda x : re.match("^([0][1-9]|[1-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/[0-9]{4}$", x)
)

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print('-> Project: ', project)
    print('-> Day: ', day)

    add_worklog(
        issue = project + '-' + custom_input("Issue Number: ", lambda x : int(x)),
        comment = custom_input("Comment: "),
        day = day,
        time_started = custom_input("Started Time [hh:mm]: ", lambda x : re.match("^([0-1][0-9]|[2][0-3]):[0-5][0-9]$", x)),
        time_spent = custom_input("Time Spent [10m, 3h]: ", lambda x : re.match("^[\d]{1,}[m,h]$", x))
    )

    custom_input("Success")
