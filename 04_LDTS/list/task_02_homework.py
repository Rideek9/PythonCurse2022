# -- TASK 2 -- Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
user_number =[]  #tego nie musiało być ale chodziło mi o to aby zebrać od użytkownika wszystkie liczby
odd_number = []
for i in range(10):
    number = int(input(f"Wybór: {i+1}  podaj liczbę całkowitą\n--> "))
    user_number.append(number)
    if number % 2 != 0:
        odd_number.append(number)

for odd in odd_number:
    print(f'Nieparzysta liczba wybrana przez użytkownika to -> {odd}')
