import figures as fig


def area(figure):
    if figure == "k":
        ar = fig.squer()
        return ar
    elif figure == 'p':
        ar = fig.rectangle()
        return ar
    elif figure == 't':
        ar = fig.triangle()
        return ar
    elif figure == 'o':
        ar = fig.circle()
        return ar


def main():
    areas = 0
    while True:
        figure = input('Jaką figurę chcesz dodać do powierzchni: k - kwadrat; p - prostokąt; t - trójkąt; o - okrąg; q - wyjście i zsumowanie\n--> ')
        if figure in ['k','p','t','o']:
            are = area(figure)
            areas += are
        elif figure == 'q':
            print(f'koniec wyliczania. Pole powierzchni budynku to {round(areas,2)}')
            break
        else:
            print('niewłaściwa figura spróbuj jeszcze raz')
            continue

main()