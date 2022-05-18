# -- TASK 3 -- W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.


txt = input("Podaj jakiś tekst")
upperLetter =0
lowerLetter = 0
number=0

for i in txt:
    if i.isupper():
        upperLetter+=1
        continue
    if i.islower():
        lowerLetter+=1
        continue
    if i.isnumeric():
        number+=1
        continue

print(f'W tekscie {txt} są następująco:\n'
      f'duże litery {upperLetter}\n'
      f'małe literu {lowerLetter}\n'
      f'cyfry {number}')



