import random
file_name = 'credit_cart.txt'

def card_generator(x):
    """x podaj długość karty """
    card_number = '\n'
    for index in range(x):
        number = random.randint(0,9)
        card_number+=str(number)
    return card_number




with open(file_name, 'a') as my_file:
    for index in range(10):
        card_number = card_generator(16)
        my_file.write(card_number)

