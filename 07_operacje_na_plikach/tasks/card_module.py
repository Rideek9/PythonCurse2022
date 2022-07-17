
def master_card(number):
    if ((5599 >= int(number[:4]) >= 5100) or (2720 >= int(number[:4]) >= 2221)) and len(number)==16:
        # print('Karta Master Card')
        return  1

def visa_card(number):
    if (4999 >= int(number[:4]) >= 4000) and ((len(number)==16) or (len(number)==13)):
        # print('Karta Visa')
        return  1

def american_express_card(number):
    if (3799 >= int(number[:4]) >= 3400) and (len(number)==15):
        # print('American Express')
        return 1

def show_card(number):
    one = master_card(number)
    two = visa_card(number)
    three = american_express_card(number)
    return one, two, three