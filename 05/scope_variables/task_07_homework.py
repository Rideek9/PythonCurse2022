# -- TASK 7 -- Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#
# Co wiemy o tych numerach tych kart?
#
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
# American Express card numbers start with 34 or 37 and have 15 digits.


def master_card(number):
    if ((5599 >= int(number[:4]) >= 5100) or (2720 >= int(number[:4]) >= 2221)) and len(number)==16:
        print('Karta Master Card')
        return  1

def visa_card(number):
    if (4999 >= int(number[:4]) >= 4000) and ((len(number)==16) or (len(number)==13)):
        print('Karta Visa')
        return  1

def american_express_card(number):
    if (3799 >= int(number[:4]) >= 3400) and (len(number)==15):
        print('American Express')
        return 1

def show_card(number):
    one = master_card(number)
    two = visa_card(number)
    three = american_express_card(number)
    return one, two, three

def is_card_exist(numbs):
    for i in numbs:
        if i == 1:
            return 'ok'


while True:
    user_card_number = input("Podaj nr swojej karty, a powiem Ci od jakiego dostawy jest ta kata\n --> ")
    test = is_card_exist(show_card(user_card_number))
    if test != 'ok':
        print('W bazie danych nie istnieje dostawca karty o podanym nr')