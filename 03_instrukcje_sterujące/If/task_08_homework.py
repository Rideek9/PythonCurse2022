# -- TASK 8 -- Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

number_one = float(input("podaj liczbę : "))
number_two = float(input("podaj liczbę : "))
number_three = float(input("podaj liczbę : "))

if number_one>number_two>number_three:
    print(f'liczba {number_one} jest największa')
    print(f'sortowanie: {number_one},{number_two},{number_three}')
elif  number_one>number_three>number_two:
    print(f'liczba {number_one} jest największa')
    print(f'sortowanie: {number_one},{number_three},{number_two}')
elif  number_two>number_one>number_three:
    print(f'liczba {number_two} jest największa')
    print(f'sortowanie: {number_two},{number_one},{number_three}')
elif  number_two>number_three>number_one:
    print(f'liczba {number_two} jest największa')
    print(f'sortowanie: {number_two},{number_three},{number_one}')
elif  number_three>number_one>number_two:
    print(f'liczba {number_three} jest największa')
    print(f'sortowanie: {number_three},{number_one},{number_two}')
elif  number_three>number_two>number_one:
    print(f'liczba {number_three} jest największa')
    print(f'sortowanie: {number_three},{number_two},{number_one}')