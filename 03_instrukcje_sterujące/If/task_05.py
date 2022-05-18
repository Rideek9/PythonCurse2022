# --TASK 5 -- Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 małą literę, 1 dużą literę i mieć długość conajmniej 8 znaków. Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input('Podaj swoje hasło:')


if len(password)<8:
    print('hasło jest za krótkie')
elif password.isalpha():
    print('hasło zawiera tylko litery')
elif password.isnumeric():
    print('hasło zawiera tylko liczby')
elif password.isupper():
    print('hasło nie ma małej litery')
elif password.islower():
    print('hasło nie ma dużej litery')
else:
    print(f'hasło {password} jest prawidowe')





