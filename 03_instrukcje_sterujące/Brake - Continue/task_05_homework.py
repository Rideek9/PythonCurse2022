# -- TASK 5 -- Stwórz grę ciepło zimno.
#
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.


import random

# variables - AI choice , number of round
AI_choice = random.randint(1, 100)
number_round = 6
i = 0

# game logic
while i < number_round:
    # user choice the number
    user_choice = int(input(f' RUNDA {i+1}:  Wybierz liczbę od 1 do 100:\n --> '))

    #  if user choice is not in the range program, program ask again user about number
    if user_choice>100 or user_choice < 1:
        print('podaj liczbę w przedziale od 1 do 100')
        continue

    #  if user find AI number the game is end and user win
    if user_choice == AI_choice:
        print(f'Znalazłeś liczbę {AI_choice} w rundzie {i+1} GRATULUJE ')
        break

    # logic game to small to large
    if user_choice<AI_choice:
        print(f" --> ZA MAŁO")
    else:
        print(f" --> ZA DUŻO")
    i+=1

# if number of rounds is exceeded user lose and program the end
if number_round==i:
    print('Wyczerpałeś limit rund . Kompyter wygrał ')