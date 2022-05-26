# -- Task 1 -- Napisz funkcje, która pyta użytkownika o pary książka + ocena i zapisuje je w programie.

books = [['Hobbit',6],["Ojciec Chrzestny",6]]

def book_rating():
    new_list =[]
    title_book = input('podaj tytuł książki: \n --> ')
    rating_book = int(input('podaj ocene książkki od 0-6 \n --> '))
    new_list.append(title_book)
    new_list.append(rating_book)
    books.append(new_list)

book_rating()

# -- Task 2 -- Napisz funkcję, która zapyta o numer książki i wyświetli tytuł wraz z oceną

def book_number():
    books_number = int(input('podaj numer książki'))
    number_not_exist(books_number)
    rating_book = books[books_number][1]
    title_book = books[books_number][0]
    print(f'Tytuł książki o nr {books_number} to {title_book} i jej ocena to {rating_book}')

# --task 3 -- W prosty sposób obsłuż bląd użytkownika - użytkownik zapyta o numer w bazie, który nie istnieje

def number_not_exist(number):
    if len(books) < number:
        print('taki nr książki nie isnieje')
        exit()


book_number()