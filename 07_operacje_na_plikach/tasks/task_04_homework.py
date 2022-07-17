import random

file_name = 'quotes.txt'

with open(file_name) as my_file:
    line = my_file.readlines()


def random_quote_list():
    x =0
    quote_list = []
    while x < 3:
        quote = random.choice(line)
        if quote in quote_list:
            continue
        else:
            quote_list.append(quote)
            x+=1
    return quote_list

def show_quote(list):
    len_txt = 100
    for index, line in enumerate(list):
        list_line = line.split('/')
        quote = list_line[0]
        author = list_line[1].replace('\n','')
        print('*' * len_txt)
        print(f'Cytaty:  {(index+1)}'.center(len_txt))
        print(quote.center(len_txt))
        print(author.center(len_txt))
        print('*' * len_txt, end='\n\n')


def main():
    show_quote(random_quote_list())


if __name__ == '__main__':
    main()


