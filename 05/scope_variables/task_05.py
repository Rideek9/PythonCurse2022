# -- TASK 05 -- Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random
number_one = 0
number_two = 20
AI_number = random.randint(number_one,number_two)
print(AI_number)

def hot_or_cold():
    while True:
        user_choise = input(f'Podaj liczbę od {number_one} do {number_two}:\n--> ')
        if user_choise.isdecimal():
            while True:
                if int(user_choise) == AI_number:
                    print("Znalazłeś liczbę. Gratuluję")
                    exit()
                else:
                    if int(user_choise) > AI_number:
                        print(f'Liczba {user_choise} jest za duża, spróbuj jeszcze raz.')
                    else:
                        print(f'Liczba {user_choise} jest za mała spróbuj jeszcze raz')
                break
        else:
            print('nie podałeś liczby, spróbuj jeszcze raz')
            continue

hot_or_cold()