list = [13,'string', True, 2.3, None,0 ]


for i in list:
    try:
        print( 10 / i)
    except Exception as err:
        print('Błąd -->  ', err)


