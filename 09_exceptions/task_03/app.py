import time

timers = time.time()
list_element = [3,'ab',True, None, False, [1,'a'],8,timers,'wss',12]


def usre_index():
    index = int(input('Podaj index od 1-10: -> '))
    return index

def division(index):
    result = 1 / list_element[index]
    return result


def main():
    index = usre_index()
    try:
        print(division(index))
    except ValueError:
        print("Value Error")
    except TypeError:
        print("Type Error")
    except ZeroDivisionError:
        print('Zero Division Error')
    except IndexError:
        print('Index Error')
        return 1

while True:
   x =  main()
   if x == 1:
       break
