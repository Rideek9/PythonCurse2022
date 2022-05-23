# -- TASK 3 -- Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

user_list = input('Podaj liczby całkowite rozdzielone przecinkami')
user_list = user_list.split(',')


if user_list[0].strip() == user_list[-1].strip():
    print('element pierwszy i ostani są takie same')
else:
    print('element pierwszy i ostani nie są takie same')