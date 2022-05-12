#---task 3 ---
'''
Do zmiennej quote przypisz zdanie:
„Honesty is the first chapter in the book of wisdom.”, a następnie:

Policz wszystkie znaki w napisie
Nie modyfikując zmiennej wyświetl słowo wisdom
Wyświetl tylko pierwszą połowę tekstu
Wyświetl tylko kropkę
Wyświetl od połowy tylko co trzecią literę cytatu
Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
Wyświetl cały cytat odwrotnie
'''


quote = "Honesty is the first chapter in the book of wisdom."

#-- 1

lenghtQuote = len(quote)
print(f'Zad1 ---> Ilość znaków w zmiennej quote wynosi {lenghtQuote}')

#--2

num_id = quote.index('wisdom')
print(f'Zad2 --> {quote[num_id:-1]}')

#--3

newLenght = lenghtQuote//2
print(f'Zad3--> pierwsza połowa tekstu to '+ quote[:newLenght])

#--4

print(f'Zad4 -->Ostatni znak to ' + quote[-1])

#--5
print(f'Zad5 -->' + quote[newLenght::3])

#--6
print(f'Zad6 --> tekst co druga litera: ' + quote[::2])

#--7
print(f'Zad7 --> cytat odwrotnie to: ' + quote[::-1])

#--8
newQuote = quote.replace('wisdom', 'friendship')
print(f'Zad8 --> nowy cytat to: ' + newQuote)



