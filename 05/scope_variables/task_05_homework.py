# -- TASK 05 -- Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random
number_one = 0
number_two = 20
AI_number = random.randint(number_one,number_two)
print(AI_number)


def too_small_number(number,AI):
    if int(number) <AI:
        print(f'Liczba {number} jest za mała, spróbuj jeszcez raz')

def too_large_number(number,AI):
    if int(number)>AI:
        print(f'Liczba {number} jest za duża, spróbuj jeszcze raz')

while True:
    user_choise = input(f'\nZnajdź liczbę z przedziału {number_one} do {number_two}:\n--> ')
    if user_choise.isdecimal():
        if int(user_choise) == AI_number:
            print(f'Znalazłeś liczbę. Gratuluje')
            break
        too_small_number(user_choise, AI_number)
        too_large_number(user_choise,AI_number)
    else:
        print('Podana wartosć nie jest liczbą, spróbuj jeszcez raz.')
        continue