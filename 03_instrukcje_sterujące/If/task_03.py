# -- TASK 3 -- twórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.


vote1 = int(input("Jak oceniasz długość książki? [0-7]: "))
vote2 = int(input("Jak oceniasz styl książki? [0-7]: "))
vote3 = int(input('Jak oceniasz sposób przedstawienia treści? [0-7]'))

voteSum = (vote1+vote2+vote3)/3

if voteSum == 7:
    print('książka bardzo dobra, warto przeczytać')
elif 7 > voteSum >= 5:
    print('książka jest przeciętna')
else:
    print('nie warto czytać książki')
