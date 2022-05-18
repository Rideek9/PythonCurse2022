# -- TASK 1 -- Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

num = int(input("podaj liczbę: "))

if num % 3 == 0:
    print(f'liczba {num} jest podzielna przez 3')
else:
    print(f'liczba {num} nie jest podzielna przez 3 zostaje {num%3} reszty')