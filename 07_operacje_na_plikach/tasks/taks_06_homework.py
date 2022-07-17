import card_module as cm

file_name ='credit_cart.txt'
visa_card = '../card/visa_card.txt'
master_card_card = '../card/master_card.txt'
america_expres_card = '../card/am_card.txt'
all_card = '../card/all_card.txt'

def what_card(visa,master,am,card):
    if visa == 1:
        with open(visa_card, 'a+') as visa:
            save_number = visa.write(card)
    elif master == 1:
        with open(master_card_card, 'a+') as master:
            save_number = master.write(card)
    elif am == 1:
        with open(america_expres_card, 'a+') as am:
            save_number = am.write(card)
    else:
        with open(all_card, 'a+') as ac:
            save_number = ac.write(card)

with open(file_name) as my_file:
    card_list = my_file.readlines()
    for card in card_list:
        new_card = card.replace('\n','')
        visa = cm.visa_card(new_card)
        master = cm.master_card(new_card)
        am = cm.american_express_card(new_card)
        what_card(visa,master,am,card)



