# -- TASK 1 -- Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
import math
def calculate_area_circle():
    radius = float(input("Podaj promień koła, a podam jego pole:\n-->"))
    P = (math.pi) * radius ** 2
    return round(P,2)

print('pole koła to', calculate_area_circle())