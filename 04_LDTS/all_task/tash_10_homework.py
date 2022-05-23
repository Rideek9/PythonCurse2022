# -- TASK 10 -- Użytkownik podaje dowolną liczbę N. Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).

user_choise = int(input('podaj liczbę całkowitą: \n--> '))
list_user=[]

for i in range(user_choise):
    i+=1
    new_list = [i,i*i]
    list_user.append(new_list)

list_user = dict(list_user)
print(list_user)