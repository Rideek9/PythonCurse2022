from bmi import calculation_BMI as calc_BMI , status_BMI as status

def user_data():
    user_height = int(input('Podaj swój wzrost w cm:\n--> '))
    user_weigt = float(input('Podaj swoją wagę w kg:\n--> '))

    return user_height,user_weigt

def advice(stat):
    if stat == 'niedowaga':
        with open('advice/niedowaga.txt') as norm:
            txt = norm.readline()
            return txt
    elif stat == 'norma':
        with open('advice/norma.txt') as norm:
            txt = norm.readline()
            return txt
    elif stat == 'nadwaga':
        with open('advice/nadwaga.txt') as norm:
            txt = norm.readline()
            return txt
    elif stat == 'otyłość':
        with open('advice/otyłosc.txt') as norm:
            txt = norm.readline()
            return txt

def main():
    user = user_data()
    BMI = calc_BMI(user[0],user[1])
    stat = status(BMI)
    adv = advice(stat)
    tt = len(adv)+10
    print('*' * tt)
    print(f"Twoje BMI to {BMI}".center(tt))
    print(adv.center(tt))
    print('*' * tt)

main()