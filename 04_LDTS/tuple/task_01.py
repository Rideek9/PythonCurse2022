# -- TASK 1 -- Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.

pet = ('pies', 'sznaucer', 'roki')
print(f'Mój {pet[0]} wabi się {pet[2].title()}, jest to {pet[1]}.')