import delta as dlt

def main():
    print('Podaj 3 wartości do obliczenia delty:')
    a = float(input('wartość a --> '))
    b = float(input('wartość b --> '))
    c = float(input('wartość c --> '))
    delta = dlt.delta_formula(a,b,c)
    print(f'Delta z liczb {a,b,c} wynosi {delta}')

main()