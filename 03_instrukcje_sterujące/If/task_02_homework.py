
# -- TASK 2 -- Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.


numbr_one= int(input('Podaj pierwszą liczbę całkowitą: '))
number_two = int(input('Podaj drugą liczbę całkowitą: '))
number_sum = numbr_one + number_two

if number_sum>100:
    print(number_sum)
else:
    print('Koniec')
