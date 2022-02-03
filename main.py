from create import create_account
from delete import delete_account
from read import read_email, read_all
from update import update_account
from help import help_func

emails = []
storage = dict()
command = ""

print("Available commands: /create /delete /update /read_email /read_all /help /close /exit")

while command != "/close":
    command = input("Enter command: ")
    if command == "/create":
        create_account(emails, storage)
    elif command == "/delete":
        delete_account(emails, storage)
    elif command == "/update":
        update_account(emails, storage)
    elif command == "/read_email":
        read_email(emails, storage)
    elif command == "/read_all":
        read_all(emails, storage)
    elif command == "/help":
        help_func()
    elif command != "/close":
        print("This is not available command. If you want to see available commands write /help")
