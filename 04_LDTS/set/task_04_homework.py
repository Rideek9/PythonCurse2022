# -- TASK 4 -- Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

elements = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
len_list = len(elements)//4
new_list =[]

for i in range(len_list):
    add_list=[]
    for a in range(4):
        add_list.append(elements[0])
        elements.pop(0)
    add_list.sort(reverse=True)
    new_list.append(add_list)

print(new_list)


