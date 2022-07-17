import os

file = 'quotes.txt'

file_size = os.path.getsize(file)

print(f'rozmiar pliku {file}: {file_size} bit')