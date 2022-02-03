from create import password_check, name_check, phone_number_check
from delete import email_check

def command_check(command):
    flag = False
    while not flag:
        flag = True
        if len(command) > 3:
            flag = False
        for i in command:
            if (i != "1") and (i != "2") and (i != "3"):
                flag = False
        if command.count("1") > 1 or command.count("2") > 1 or command.count("3") > 1:
            flag = False
        if command == "/exit":
            flag = True
        if not flag:
            command = input("This command is not available. Please, enter correct comand: ")
    return command

def update_account(emails, storage):
    command = input("What do you want to update?\n1 - name\n2 - password\n3 - phone number\nPlease, enter the number. You can enter several commands." +
                    " For example, 12 (update name and password)\nYou can not to update email\n")
    command = command_check(command)
    if command == "/exit":
        return
    email = input("Enter account's email: ")
    email = email_check(email, emails)
    if email == "/exit":
        return
    if "1" in command:
        name = input("Enter new name: ")
        name = name_check(name)
        if name == "/exit":
            return
    else:
        name = storage[email]["name"]
    if "2" in command:
        password = input("Enter new password: ")
        password = password_check(password)
        if password == "/exit":
            return
    else:
        password = storage[email]["password"]
    if "3" in command:
        phone_number = input("Enter new phone number: ")
        phone_number = phone_number_check(phone_number)
        if phone_number == "/exit":
            return
    else:
        phone_number = storage[email]["phone number"]
    storage[email]["name"] = name
    storage[email]["password"] = password
    storage[email]["phone number"] = phone_number