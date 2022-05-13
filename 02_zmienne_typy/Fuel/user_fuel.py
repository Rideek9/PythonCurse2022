priceOfFuel = float(input("Podaj cenę paliwa za litr: "))
usage_fuel = float(input("Podaj spalanie samochodu na 100km: "))
distance = int(input("podaj dystans do przejechania: "))

cost = ((usage_fuel / 100) * distance) * priceOfFuel

print(f'koszt paliwa na trasę o długości {distance}km to {round(cost,2)} zł')