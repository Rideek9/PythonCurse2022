priceOfFuel = 5.04
usage_fuel = 6.4
distance = 120

cost = ((usage_fuel / 100) * distance) * priceOfFuel

print(f'koszt paliwa na trasę o długości {distance}km to {round(cost,2)} zł')