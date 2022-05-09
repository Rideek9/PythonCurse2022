userKg = float(input('podaj swoją wagę w kg: '))
userHeight = float(input('podaj swój wzrost w cm: '))
bmi = (userKg)/((userHeight / 100) ** 2)

print(f'Twoje BMI to: {round(bmi, 2)}')