# -- TASK 3 -- Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

tuple_one = ('a','b','c','d','e','f','g',11,14,16)
tuple_two = (11,12,13,14,15,16,17,18,'a','b','c')

odd_list = tuple_one[::2]+tuple_two[::2]
even_list = tuple_one[1::2]+tuple_two[1::2]

print(odd_list)
print(even_list)

print(set(odd_list))
print(set(even_list))