# -- TASK 3 -- Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

n =5
tab =[["1"]* n]*n

for i in tab:
    for a in range(len(i)):
        print(i[a], end=" ")
    print()