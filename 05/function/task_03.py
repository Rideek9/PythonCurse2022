# --  TASK 3 --   Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

user_numbers = input("podaj liczby całkowite rozdzielone prezcinkami:\n-->")
new_list= user_numbers.split(',')

def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum+= int(number)
    return sum

print(sum_list(new_list))