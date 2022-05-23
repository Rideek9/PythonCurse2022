# -- TASK 2 --  Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1,2,3,4]
T_test = (1,2,3,4)
S_test = {1,2,3,4}

# w większości będą działać wszystkie metody z wyjątkiem metod zmieniających listę czyli append i remove z czego remove dla Setów działa natomiast aby dodadać do Seta element trzeba użyć metody add nie append jak w przypadku listy gdzie przy liscie metoda add nie występuje. Przy

S_test.append(3) #metoda nie występuje
T_test.remove(3) #metoda nie występuje nie można modyfikować krotki bez obejścia
T_test.append(3) #metoda nie występuje nie można modyfikować krotki bez obejścia
T_test.add(3) #metoda nie występuje nie można modyfikować krotki bez obejścia
