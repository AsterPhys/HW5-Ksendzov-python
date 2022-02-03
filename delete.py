
def email_check(email, emails):
    flag = False
    while not flag:
        flag = True
        if email != "/exit":
            if len(email) == 0:
                email = input("This email is empty. Please, enter another email: ")
                flag = False
            if flag and email not in emails:
                email = input("This email was not found in storage. Please, enter another email: ")
                flag = False
        else:
            flag = True
    return email

def delete_account(emails, storage):
    email = input("Enter email of account, that you want to delete: ")
    email = email_check(email, emails)
    if email == "/exit":
        return
    emails.remove(email)
    storage.pop(email)