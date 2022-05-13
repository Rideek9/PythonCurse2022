# -- TASK 2 -- Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym. Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).

bin_num = 1001111
new_num= str(bin_num)

#Ogólnie zrobił bym to pętlom ale że nie mieliśmy jeszcze tego zagadnienia to zrobiłem to w ten sposób
number = 2**0*int(new_num[-1])+2**1*int(new_num[-2])+2**2*int(new_num[-3])+2**3*int(new_num[-4])+2**4*int(new_num[-5])+2**5*int(new_num[-6])+2**6*int(new_num[-7])


print(f'Liczba binarna {bin_num} w stystemie dziesiętnym daje wynik {number}')

