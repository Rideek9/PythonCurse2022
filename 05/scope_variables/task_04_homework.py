# -- TASK 4 -- Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def is_number_in_range(number,list_number):
    if number in list_number:
        return f'Liczba {number} występuje w zakresie'
    else:
        return f'Liczba {number} nie występuje w zakresie'

list_numbers = [1,2,3,4,5,6,7,8,9,10]
user_number = int(input("Podaj liczbę: \n--> "))
print(is_number_in_range(user_number, list_numbers))