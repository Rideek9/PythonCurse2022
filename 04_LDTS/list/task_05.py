# -- TASK 5 -- Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

persons =[
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'skoczek narciarski'],
    ['Johny', 'Deep', 'aktor'],
    ['Mikołaj', 'Kopernik', 'astronom']
]

# for person in persons:
#     print(f'{person[0]} {person[1]} --> {person[2]} ')

for person in persons:
    for id, value in enumerate(person):
        if id == 2:
            print("|", value)
        else:
            print(value, end=' ')

