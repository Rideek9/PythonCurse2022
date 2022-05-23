# -- TASK 5 --  Porównaj zachowanie discard() vs remove() dla typu set.

s_list ={1,2,3,4,5,6,7,8,9}

print(s_list)
s_list.discard(12)
print(s_list)

s_list.remove(5)
print(s_list)

# te dwie metody działają podobnie usuwają element wskazany przez użytkownika, z tym że metoda remove() zwróci błąd jeśłi dany element nie istnieje natomias metoda discard() błędu nie zwróci jeśli dany element nie istnieje