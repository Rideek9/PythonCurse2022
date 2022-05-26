# -- TASK 4 -- Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)
import random
from task_02_homework import is_number_even

all_numbers = []
#tworzenie listy elementów
for i in range(20):
    number = random.randint(1,100)
    all_numbers.append(number)

#sprawdzenie czy element jest parzysty
for number in all_numbers:
    even_number = is_number_even(number)
    if even_number != None:
        print(even_number)
