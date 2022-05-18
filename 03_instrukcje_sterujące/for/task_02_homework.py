# -- TASK 2 -- Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

components = ['pulpa mango', 'miód' ,'jogurt naturalny', 'kardamon']

print('do naczynia wrzuć\n')
for i in range(len(components)):
    print(f'krok {i+1} wrzuć --> {components[i]}')
print('Dokładnie wymieszaj')
print('\nMango Lassi najlepiej smakuje schłodzone')