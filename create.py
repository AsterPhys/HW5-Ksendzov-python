from string import punctuation, ascii_letters

def email_check(emails, email):
    flag = False
    while not flag:
        flag = True
        if email != "/exit":
            if email in emails:
                email = input("This email has already created. Please, enter another email: ")
                flag = False
            if flag and email == "":
                email = input("This email is empty. Please, enter another email: ")
                flag = False
            if flag and "@gmail.com" not in email and "yandex.ru" not in email and "mail.ru" not in email:
                email = input("We don't provide this email-service. Please, use gmail, mail or yandex: ")
                flag = False
            if flag and len(email) > 320:
                email = input("This email is too long. Please, enter another email: ")
                flag = False
            if flag and not(email[len(email) - 10 : ] == "@gmail.com" or email[len(email) - 10 : ] == "@yandex.ru" or email[len(email) - 8 : ] == "@mail.ru"):
                email = input("We don't provide this email-service. Please, use gmail, mail or yandex: ")
                flag = False
            if flag and "gmail.com" in email and len(email) == 10:
                email = input("This is not valid email. Please, enter another email: ")
                flag = False
            if flag and "yandex.ru" in email and len(email) == 10:
                email = input("This is not valid email. Please, enter another email: ")
                flag = False
            if flag and "mail.ru" in email and len(email) == 8:
                email = input("This is not valid email. Please, enter another email: ")
                flag = False
        else:
            flag = True
    return email

def name_check(name):
    flag = False
    while not flag:
        flag = True
        if name != "/exit":
            if len(name) == 0:
                name = input("This name is empty.  Please, enter another name: ")
                flag = False
            if flag and not(name.isalpha()):
                name = input("Name can contain only latin letters.  Please, enter another name: ")
                flag = False
        else:
            flag = True
    return name

def password_check(password):
    flag = False
    while not flag:
        flag = True
        if password != "/exit":
            if len(password) == 0:
                password = input("This password is empty. Please, enter another password: ")
                flag = False
            if flag:
                for i in punctuation:
                    if i in password:
                        break
                else:
                    password = input("This password doesn't contain special symbols (punctuation).\nPassword" +
                                     " must have at least 1 special symbol, 1 letter and 1 number.\nPlease, enter another password: ")
                    flag = False
            if flag:
                for j in "0123456789":
                    if j in password:
                        break
                else:
                    password = input("This password doesn't contain numbers.\nPassword" +
                                     " must have at least 1 special symbol, 1 letter and 1 number.\nPlease, enter another password: ")
                    flag = False

            if flag:
                for z in ascii_letters:
                    if z in password:
                        break
                else:
                    password = input("This password doesn't contain letters.\nPassword" +
                                     " must have at least 1 special symbol, 1 letter and 1 number.\nPlease, enter another password: ")
                    flag = False
        else:
            flag = True

    return password

def phone_number_check(phone_number):

    flag = False
    while not flag:
        flag = True
        if phone_number != "/exit":
            if len(phone_number) == 0:
                phone_number = input("This phone number is empty. Please, enter another phone number: ")
                flag = False
            if flag and not(phone_number[0] == "8" or phone_number[:2] == "+7"):
                phone_number = input("We provide only russian numbers (starting with 8 or +7). Please, enter another phone number: ")
                flag = False
            if flag and phone_number[0] == "8" and len(phone_number) != 11:
                phone_number = input("This phone number is not correct. Please, enter another phone number (fe: 88005553535 or +78005553535): ")
                flag = False
            if flag and phone_number[:2] == "+7" and len(phone_number) != 12:
                phone_number = input("This phone number is not correct. Please, enter another phone number (fe: 88005553535 or +78005553535): ")
                flag = False
            if flag and phone_number[0] == "8":
                try:
                    phone_number = input("This phone number is not correct. Please, enter another phone number (fe: 88005553535 or +78005553535): ")
                    int(phone_number[1:])
                except:
                    flag = False
            if flag and phone_number[:2] == "+7":
                try:
                    phone_number = input("This phone number is not correct. Please, enter another phone number (fe: 88005553535 or +78005553535): ")
                    int(phone_number[2:])
                except:
                    flag = False
        else:
            flag = True
    return phone_number

def create_account(emails, storage):
    email = input("Enter email: ")
    email = email_check(emails, email)
    if email == "/exit":
        return
    name = input("Enter name: ")
    name = name_check(name)
    if name == "/exit":
        return
    password = input("Enter password: ")
    password = password_check(password)
    if password == "/exit":
        return
    phone_number = input("Enter phone number: ")
    phone_number = phone_number_check(phone_number)
    if phone_number == "/exit":
        return
    emails.append(email)
    storage[email] = {"name": name, "password": password, "phone number": phone_number}