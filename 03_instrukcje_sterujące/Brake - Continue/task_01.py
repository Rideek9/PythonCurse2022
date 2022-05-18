# -- TASK 1 -- Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.

names = input('Podaj imiona, rozdziel je przecinkiem')

nameList = names.split(',')

for name in nameList:
    print(f'Witam {name}')




