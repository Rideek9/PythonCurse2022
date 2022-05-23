# -- TASK 7 - Usuń duplikaty z podanej listy i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

st = [34,17,25,41,12,194,41,3,12,99,94]

new_st = sorted(tuple(set(st)))

print(f'Najmniejsza wartość to {new_st[0]}, a największ to {new_st[-1]}')

