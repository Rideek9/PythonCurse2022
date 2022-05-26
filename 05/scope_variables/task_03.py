# -- TASK 03 -- Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_number(a,b,c):
    lists=[a,b,c]
    lists.sort()
    return lists[-1]

print(max_number(1,4,3))