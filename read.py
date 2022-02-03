from delete import email_check

def read_email(emails, storage):
    email = input("Enter email to see user's information: ")
    email = email_check(email, emails)
    if email == "/exit":
        return
    print("Email: " + email, end=" ")
    print("Name: " + storage[email]["name"], end=" ")
    print("Password: " + storage[email]["password"], end=" ")
    print("Phone number: " + storage[email]["phone number"], end=" ")
    print()

def read_all(emails, storage):
    j = 0
    pass1 = input("Enter the password of required level: ")
    while (pass1 != "Not hehe") and (pass1 != "/exit") and j < 3:
        j += 1
        if j == 3:
            return
        pass1 = input(f"Wrong password. You have more {3 - j} tries: ")
    i = 1
    for email in emails:
        print(f"{i}) ", end="")
        print("Email: " + email, end=" | ")
        print("Name: " + storage[email]["name"], end=" | ")
        print("Password: " + storage[email]["password"], end=" | ")
        print("Phone number: " + storage[email]["phone number"], end="")
        print()
        i += 1
    if len(emails) == 0:
        print("The storage is empty")