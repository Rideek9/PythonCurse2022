# -- TAASK 01 -- Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.


user_weight = float(input('podaj swoją wagę:\n-->'))
user_height = int(input('podaj wzrost w cm:\n-->'))

def BMI_calculator(height, weight):
    BMI = weight /((height/100)**2)
    return round(BMI,2)


def your_bmi_status(BMI):
    if BMI < 18.5:
        return "niedowaga"
    elif BMI <25:
        return "norma"
    elif BMI< 30:
        return "nadwaga"
    else:
        return "otyłość"

your_BMI = BMI_calculator(user_height,user_weight)

print(f'Twoje BMI to {your_BMI} jest to {your_bmi_status(your_BMI)}')