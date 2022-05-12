# --- task4 ---
'''
Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
-Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
-Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
-Połącz dane w jeden ciąg book za pomocą spacji
-Policz liczbę wszystkich znaków w napisie book

'''

bookTitle = input('Podaj nazwę książki: ').title()
bookAuthor = input('Podaj nazwisko autora: ').title()
bookLenght = input("Podaj liczbę stron książki: ")

#zad1 -- Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.

isLetters = bookTitle.isalpha() and bookAuthor.isalpha() and bookLenght.isnumeric()
print(f'Czy dane są prawidłowe? --> {isLetters}')

#zad2 -- Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print(bookTitle,bookAuthor)

#zad3 --Połącz dane w jeden ciąg book za pomocą spacji
book = f'{bookTitle} {bookAuthor} {bookLenght}'
print(book)

#zad4 --- Policz liczbę wszystkich znaków w napisie book
print(f'Długość wszystkich znaków to: {len(book)}')