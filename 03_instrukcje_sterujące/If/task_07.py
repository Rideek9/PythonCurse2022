# -- TASK 7 -- Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

user_height = int(input('podaj swój wzrost w cm:'))
user_weight = float(input('podaj swoją wagę: '))
BMI = user_weight/((user_height/100)**2)
BMI = round(BMI,2)

print(BMI)
if 18.5>BMI:
    print("Niedowaga")
elif 24.9>=BMI>=18.5:
    print('Prawidłowa masa ciała')
elif 29.9>=BMI>=25:
    print("nadwaga")
elif 34.9 >=BMI>=30:
    print("otyłość I stopnia")
elif 39.9>=BMI>=35:
    print("otyłość II stopnia")
else:
    print("otyłość III stopnia")