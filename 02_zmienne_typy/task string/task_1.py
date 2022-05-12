#--- task 1 --- Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

word = 'hakunamatata'

lgh = len(word)//2
first_id = lgh - 1
second_id = lgh + 1

print(word[first_id:second_id + 1])

