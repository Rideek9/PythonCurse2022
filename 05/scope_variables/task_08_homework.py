# -- TASK 8 -- Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# marka (str)
# model (str)
# rocznik (int)
# Wypisze ten słownik na ekran (bez żadnego formatowania)
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.

car = {
    'marka' : 'Mercedes',
    'model' : 'C123',
    'rocznik' : 1979
}

def monument_car(marka,model,rocznik):
    print(f'{marka} {model} rocznik {rocznik}')
    if (2021 - rocznik) > 25:
        print(f'Gratulacje! Twój samochód {marka} może być zarejestrowany jako zabytek')
    else:
        print(f'Twój samochód {marka} jest jeszcze zbyt młody')

monument_car(car['marka'],car['model'],car['rocznik'])
