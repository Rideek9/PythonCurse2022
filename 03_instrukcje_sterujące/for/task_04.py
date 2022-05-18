# -- TASK 4 -- Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

number = int(input('Podaj liczbę do 8: '))

n=1
for i in range(number):
    k = i+1
    n*=k
print(n)