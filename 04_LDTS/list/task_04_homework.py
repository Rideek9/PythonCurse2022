# -- Task 4 -- Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

while True:
    user_element = input('Podaj parzystą ilość elementów rozdzielonych przezcinkiem:\n--> ')
    list_element = user_element.split(',')
    len_list_element = len(list_element)
    if len_list_element% 2 == 0:
        center_index = len_list_element // 2
        if list_element[center_index] == list_element[center_index-1]:
            print(f"Element {list_element[center_index]} i element {list_element[center_index-1]} są takie same")
        else:
            print(f"Element '{list_element[center_index]}' i element '{list_element[center_index - 1]}' nie są takie same")
        break
    else:
        print('Podałeś niepażystą liczbę elementów, powtórz wrowadzenie elementów')
        continue
