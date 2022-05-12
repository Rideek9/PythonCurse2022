txt = "Pythonjestsuper"
numb = '123456'
center = 'mata'
ban = 'banana'

print(txt[0])
print(txt[0:8])
print(txt[:9:2])
print(txt[-1])
print(txt[-5:-1]+txt[-1])
print(txt[:10] + txt[10:])

print(txt.replace('Py','W'))


#------------ praca z dokumentacją
print(numb.isnumeric())
print(center.center(20,'*'))
print(txt.rstrip('super'))
test = txt.isalpha() and (not txt.islower() and not txt.isupper())
print(test)
print(ban.count('na'))
