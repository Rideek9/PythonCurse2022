# -- TASK 4 -- Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

word = 'Alicja'

if len(word)>5:
    print(f'ciąg "{word}" jest dłuższy niż 5 znaków')
    if word.count('a'):
        print(f'ciąg "{word}" zawiera litere "a" --> zamieniam literę "a" na "z"')
        new_word = word.replace('a','z')
        print(f'"{new_word}"')
    else:
        print(word)
else:
    print('Ciąg znaków jest mniejszy niż 5')

