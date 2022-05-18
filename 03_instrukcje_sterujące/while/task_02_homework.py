# -- TASK 2 --  Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_number = 5
round = 1
flag = True


while flag:
    print(f' runda: {round}')
    user_number = int(input('podaj liczbę od 1-20: '))
    if secret_number == user_number:
        flag = False
        print(f"Znalazłeś sekretną liczbę {secret_number} ")
        if round == 1:
            print(f'Odgadnięcie liczby zajęło Ci 1 rundę')
        elif 4>=round>1:
            print(f'Odgadnięcie liczby zajęło Ci {round} rudny')
        else:
            print(f'Odgadnięcie liczby zajęło Ci {round} rund')
    round+=1


