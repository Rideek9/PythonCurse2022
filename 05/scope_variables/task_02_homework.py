# -- TASK 02 -- Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def min_fun(a, b, c):
    valu1 = a if a < b else b
    valu1 = c if c < valu1 else valu1
    return valu1


