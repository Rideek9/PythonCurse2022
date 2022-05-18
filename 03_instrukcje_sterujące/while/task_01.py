# -- TASK 1 --Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

print('--------Pętla WHILE-------\n')

F = 0
while F<=200:
    C=5/9*(F-32)
    print(f'{F} st Faranchajta to {round(C,2)} st celcjisza')
    F+=20

print('\n-----Pętla FOR------\n')
for i in range(0,201,20):
     print(f'{i} st Farenchajta to {round((5/9*(i-32)),2)} st Celcjusza')
