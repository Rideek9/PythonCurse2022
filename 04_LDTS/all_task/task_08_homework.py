# -- TASK 8 -- Utwórz słownik dla 10 krajów Europy zawierający listy 10 najpopularniejszych imion żeńskich. Zapisz imiona w wersji anglojęzycznej. Dodaj wszystkie listy razem. Nowa lista powinna zawierać 100 elementów.

country_names = {'Portugalia':	['Ann',	'Barbra','Dorothy','Elizabeth','Eva','Frances','Isabelle','Lily','Martha','Lucy'],
'Polska':['Aline','Angelica','Dorothy','Edith','Elizabeth','Eva','Ilona','Marissa','Olivie','Julie'],
'Niemcy':	['Antoinette','Elizabeth','Eva','Isabelle','Judy','Lily','Marissa','Martha','Sandy','Lucy'],
'Anglia': ['Angelica','Antoinette','Barbra','Kate','Eva','Isabelle','Janet','Judy','Marissa','Lucy'],
'Belgia': ['Agatha','Barbra','Elizabeth','Frances','Hannah','Isabelle','Marissa','Martha','Vivian','Lucy'],
'Włochy': ['Angelica','Ann','Barbra','Kate','Dorothy','Elizabeth','Emily','Hannah','Ilona','Olivie'],
'Francja': ['Barbra','Dorothy','Elizabeth','Hilda','Judy','Lily','Martha','Sandy','Lucy','Sophia'],
'Hiszpania': ['Ann','Barbra','Kate','Dorothy','Edith','Frances','Hannah','Ilona','Isabelle','Olivie'],
'Dania': ['Aline','Angelica','Dorothy','Frances','Isabelle','Janet','Joan','Olivie','Sandy','Vivian'],
'Filandia': ['Aline','Dorothy','Frances','Hannah','Marissa','Martha','Olivie','Sandy','Julie','Sophia']}

new_list=[] #lista wszstkich imion ze wszysktich ktajów

# Funkcja tworząca nową listę imion wszystkich krajów
for index in country_names.values():
    new_list.extend(index)

set_list = set(new_list) #usunięcie duplikatów imion
most_popular_name =[] # stworzenie listy najbardziej popularnych imion w europie

for index in set_list:
    if new_list.count(index)>=3:
        print(f' Imie {index} wystąpiło w {new_list.count(index)} krajach')
        most_popular_name.append(index)
