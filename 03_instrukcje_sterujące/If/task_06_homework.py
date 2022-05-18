# -- TASK 6 -- Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.


hidden_number = 55
user_number = int(input('Podaj liczbę z przediału 1-100 i sprawdź czy zgadniesz o jakiej liczbie myślę: '))

if hidden_number == user_number:
    print('Gratulacje!, zgadłeś')
else:
    print("Pudło!, może innym razem")