# -- TASK 2 -- Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).


user_txt = input('Podaj jakiś tekst: ')
new_txt = ""

for i in range(1,len(user_txt),2):
    new_txt+=user_txt[i]

print(f'Wyświetlenie przystych znaków  wykorzystując pętle WYNIK: -->', new_txt)


new_txt_second = user_txt[1::2]
print(f'Wyświetlenie przystych znaków nie wykorzystując pętli WYNIK: -->', new_txt_second)