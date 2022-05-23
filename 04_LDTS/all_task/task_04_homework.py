# -- TASK 4 -- Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.


for i in range(10):
    for a in range(10):
        print(f'{(i+1)*(a+1)}', end=' | ')
    print()

