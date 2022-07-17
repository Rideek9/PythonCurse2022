file = 'quotes.txt'

with open(file) as myfile:
    for x in range(5):
        line = next(myfile)
        print(f'{x+1}: ',line.replace('\n','').replace('/','-- author --> '))

