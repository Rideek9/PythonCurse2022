#--Presentatnion task --- Poproś użytkownika o podanie 3 przedmiotów oraz ocenę jaką z nich uzyskał
#--od siebie dodałem wyliczanie średniej aby zobaczyć czy wyszliśmy z pętli


avargate = 0
for i in range(3):
    subject = input("Podaj nazwę przedmiotu: ")
    grade = int(input(f'Podaj ocenę z {subject}: '))
    print(f'Ocena z {subject} to {grade}')
    avargate+=grade

print(f'Twoja średnia ocen z 3 przedmiotów to {round(float( avargate / 3), 2)}')

