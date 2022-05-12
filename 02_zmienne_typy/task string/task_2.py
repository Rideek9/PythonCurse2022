# --- task 2--- Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = 'Samochód'
s2 = 'Drzewo'

s1Len= len(s1)//2

print((s1[:s1Len]+s2+s1[s1Len:]).lower())