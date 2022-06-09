import random


def today_quote(file):
    with open(file) as quotes:
        contents = quotes.readlines()
    quote = random.choice(contents).strip("\n")
    len_quote = len(quote)+20
    quote_author = quote.split('/')
    author = f'Author: {quote_author[1]}'
    print('*'* len_quote)
    print(quote_author[0].center(len_quote))
    print(author.center(len_quote))
    print('*'* len_quote)

today_quote('quotes.txt')