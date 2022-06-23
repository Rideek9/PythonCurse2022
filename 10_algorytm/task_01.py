

def user_email():
    while True:
        user = input(f'Podaj szukanego maila\n-->  ')
        if "@" in user:
            return user
            break
        else:
            print("podana nazwa nie jest mailem, spróbuj jeszcze raz")


def email_list():
    mail_list = []
    with open('mail.txt') as mail:
        for element in mail:
            mail_list.append(element.replace("\n",""))
    return mail_list


def verification(user, list_mail):
    for email in list_mail:
        if user == email:
            return f'Mail {user} istnieje na liście'
    return  f"Mail {user} nie istnieje na liście"


def main():
    user = user_email()
    list_mail = email_list()
    print(verification(user,list_mail))



main()