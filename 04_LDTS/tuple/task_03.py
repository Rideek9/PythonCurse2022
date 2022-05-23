# -- TASK 3 -- Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

number = (10,12,5,3,22,18,3,6)

user_number = int(input("podaj liczbę całkowitą --> "))

if number.count(user_number):
    print(f'liczba {user_number} isnieje w zbiorze, znajduje się na indeksie {number.index(user_number)}')
else:
    print(f'liczba {user_number} nie znajduje się w zbiorze')


# if user_number in number:
#     print(f"liczba {user_number} jest na liście pod indesem {number.index(user_number)}")
# else:
#     print(f'liczba {user_number} nie znajduje się w zbiorze')

