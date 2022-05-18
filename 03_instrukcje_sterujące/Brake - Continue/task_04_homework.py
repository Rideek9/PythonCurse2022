# -- TASK 4 --- Napisz grę - kamień (k) / papier (p) / nożyce (n).
#
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

win_user = 0
win_AI = 0
draw = 0
how_many_round = 1
user_round = 1
while True:

    # the program end the game when the number of user select round is exceed
    # and show result who win or draw
    if user_round < how_many_round:
        print('Wykożystałeś wszystkie rundy. Do zobaczenia')
        print(f'Wyniki:\n'
              f'ilość rund: {how_many_round-1}\n'
              f'wygranych użytkownika: {win_user}\n'
              f'wygranych komputera: {win_AI}\n'
              f'ilość remisów: {draw}')
        if win_user == win_AI:
            print('Remis')
        elif win_user>win_AI:
            print('Wygrał użytkownik, GRATULACJE!')
        else:
            print('Wygrał komputer, NIESTETY MOŻE INNYM RAZEM')
        user_round = 1
        break

    # user choices and AI choices to start the game
    print(f'RUND: {how_many_round}')
    if user_round == 1:
        how_round = int(input("ile rund chcesz grać\n Wybór --> "))
        user_round = how_round
    user_choise = input("\nWpisz odpowiedni znak: k - kamień , p - papier, n - nożyczki , q - wyjście \nWYBÓR--> ")
    AI_list = ['k','p','n']
    AI_choise = AI_list[int((random.random()*len(AI_list))//1)]
    print(user_round)

    # quit the game and show result when user choise q
    if user_choise == 'q':
        print('Użytkownik zakończył grę. Do zobaczenia')
        print(f'Wyniki:\n'
              f'ilość rund: {how_many_round}\n'
              f'wygranych użytkownika: {win_user}\n'
              f'wygranych komputera: {win_AI}')
        user_round = 1
        break


    # the game logic, program checks who win or draw. Next add increment to result. And increase round
    if user_choise == AI_choise:
        print('Remis')
        draw+=1
    elif (user_choise == 'k' and AI_choise == 'n') or (user_choise=='n' and AI_choise == 'p') or (user_choise == 'p' and AI_choise == 'k'):
        print('Użytkownik wygrał')
        win_user+=1
    else:
        print('Komputer wygrał')
        win_AI+=1

    how_many_round+=1




