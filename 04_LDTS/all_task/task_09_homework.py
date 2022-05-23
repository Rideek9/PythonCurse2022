# -- TASK 9 -- 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach. Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)


user_dict ={}
for user in range(5):
    user_choise = input('podaj cztery ulubione przedmioty rozdzielone przecinkami:\n --> ').lower()
    new_list = list(user_choise.split(','))
    if len(new_list)<4:
        print('podałeś zmyt mało przedmiotów, spróbuj jeszcze raz.')
        continue
    user_dict[f'Uczeń {user+1}'] = new_list

new_lists = user_dict.values()
all_list = []

for element in new_lists:
    all_list.extend(element)

convert_list = sorted(list(set(all_list)))
popular_subject = {}

for element in convert_list:
    popular_subject[element] = all_list.count(element)

print(popular_subject)


