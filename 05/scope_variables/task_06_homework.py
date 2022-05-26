# -- TASK 6 -- Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
import random

user_wins = 0
AI_wins = 0
draw = 0
rounds = 1
possibilities = ['k', 'p', 'n','q']

def wins(user,AI):
    if (user == 'p' and AI == 'k') or (user == 'k' and AI == 'n') or (user == 'n' and AI =='p'):
        print('Wygrałeś, punkt dla Ciebie :)')
        return 'win'
    elif (user == 'p' and AI == 'n') or (user == 'k' and AI == 'p') or (user == 'n' and AI =='k'):
        print('Przegrałeś, punkt dla komputera :(')
        return 'lose'
    else:
        print('Remis :|')
        return 'draw'


def end_game(chosie):
    if chosie == 'q':
        print('\nzakończyłeś grę')
        print(f'Wygrałeś: {user_wins} razy')
        print(f'Przegrałeś {AI_wins} razy')
        print(f'Zremisowałeś: {draw} razy')
        if user_wins == AI_wins:
            print('Ogólny wynik to --> REMIS')
        elif user_wins > AI_wins:
            print('Ogólny wynik to --> WYGRANA')
        else:
            print('Ogólny wynik to --> PRZEGRANA')
        exit()

while True:
    print('Wybierz: k - kamień, p - papier, n - nożyczki, q - wyjście')
    user_choise = input('--> ')
    AI_choice = random.randint(0,len(possibilities)-1)
    AI_choice_two = possibilities[AI_choice]
    if user_choise not in possibilities:
        print('podałeś złą wartość, spróbuj jeszcze raz.')
        continue
    end_game(user_choise)
    test = wins(user_choise, AI_choice_two)
    if test == 'win':
        user_wins+=1
    elif test == 'lose':
        AI_wins+=1
    else:
        draw+=1
