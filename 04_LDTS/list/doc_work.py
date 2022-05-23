# --TASK 1 -- Metoda która utworzy kopię listy
import copy
list = [1,2,3,4]

lista=list
newList = list.copy()
deeplist = copy.deepcopy(list)
print(id(list))  # -  id pamięci 140724335346432
print(id(newList)) # -  id pamięci 140724335339776
print(id(lista)) # -  id pamięci 140724335346432
print(id(deeplist)) # - id pamięci 140724335339520

#--TASK 2 -- Metoda która posortuje tablicę

listSecond = [9,2,5,4,1,0,12]
sortList = sorted(listSecond)
print(sortList)


#--TASK 3 -- Jaka metoda usunie wszystkie elementy z listy

listThird = [1,2,3,4,5,6,7]
listThird.clear()


#--TASK 4 -- Policz wystąpienia tego samego elementu w tablicy

#--TASK 5 -- Zsumuj liczby na liście

