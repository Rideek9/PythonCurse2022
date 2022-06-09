""" show your BMI and retur your status """

def calculation_BMI(height, weigt):
    your_BMI = weigt / ((height/100)**2)
    return  round(your_BMI,2)


def status_BMI(BMI):
    if BMI < 18.5:
        return 'niedowaga'
    elif 24.9 > BMI > 18.5:
        return 'norma'
    elif 29.9 > BMI > 25:
        return 'nadwaga'
    else:
        return 'otyłość'



