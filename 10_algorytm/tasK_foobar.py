def FooBar(n):
    for i in range(1,n+1):
        if (i % 3) == 0 and (i % 5) == 0:
            print('FooBar')
        elif (i % 5) == 0:
            print("Bar")
        elif  (i % 3) == 0:
            print('Foo')
        else:
            print(i)

FooBar(15)