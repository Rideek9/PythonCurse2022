# -- TASK 2 -- Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

element_tuple = ('a','b','c',1,2,3,4,5,'d','e','f',6,7,8,'a','b','c','e',8,8,6,3)

for element in element_tuple:
    if element_tuple.count(element)>1:
        print(f'Element {element} występuje {element_tuple.count(element)} razy')

