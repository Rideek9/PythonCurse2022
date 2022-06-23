def printing(n):
    if n < 0:
        print('-')
        n -= n
    if (n / 10) != 0:
        printing(n/10)
    print(n % 10)


printing(10)