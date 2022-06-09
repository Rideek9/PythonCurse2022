import os.path as osp

def open_file(file):
     full_file = f'{file}.txt'
     if osp.exists(full_file):
          if osp.getsize(full_file) >0:
               with open(full_file, 'r') as fil:
                    document = fil.read()
                    print(document)
          else:
               print('Plik jest pusty')
     else:
          print('Plik nie istnieje, tworzę plik')
          with open(full_file, 'w') as fil:
               fil.write('')


def add_to_file():
     file = input('Podaj plik do którego chcesz coś dopisać:\n--> ')
     with open(file, 'a') as fil:
          txt = input("Podaj co chcesz dopisać:\n--> ")
          fil.write(f'\n{txt}')


