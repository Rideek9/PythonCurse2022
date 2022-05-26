# --TASK 9 -- Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
# ponownie wyświetl zmieniony słownik
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.


car = {
    'marka' : 'Mercedes',
    'model' : 'C123',
    'rocznik' : 1979
}
car['czy_oryginalny'] = True

def monument_car(marka,model,rocznik,oryginal):
    print(f'{marka} {model} rocznik {rocznik}')
    if (2021 - rocznik) > 25 and oryginal:
        print(f'Gratulacje! Twój samochód {marka} może być zarejestrowany jako zabytek')
    elif (2021 - rocznik) > 25 and not oryginal:
        print(f'Twój samochód {marka} ma odpowiedni rocznik ale nie ma 75% oryginalnych części')
    elif (2021 - rocznik) <= 25 and oryginal:
        print(f'Twój samochód {marka} jest jeszcze zbyt młody ale ma 75% oryginalnych części')
    else:
        print(f'Twój samochód {marka} jest jeszcze zbyt młody i nie ma 75% oryginalnych części')

monument_car(car['marka'],car['model'],car['rocznik'],car['czy_oryginalny'])

