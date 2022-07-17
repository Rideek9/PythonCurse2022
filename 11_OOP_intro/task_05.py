class Shop:
    def __init__(self,product=[]):
        self.product = product

    def see_item(self,user_item):
        for item in self.product:
            if user_item == item:
                return f'patrzę na {item}'

    def try_on_item(self, try_on_item):
        for item in self.product:
            if try_on_item == item:
                return f'przymierzam {item}'

    def buy_item(self, buy_item):
        if buy_item in self.product:
            index = self.product.index(buy_item)
            return f'kupiłem {self.product.pop(index)}'

    def return_item(self,item):
        self.product.append(item)
        return f'Oddaje {item}'



store = Shop(['koszulka', 'spodnie', 'sweter', 'rękawiczki'])

print(store.product)
print(store.see_item('koszulka'))
print(store.try_on_item('spodnie'))
print(store.buy_item('rękawiczki'))
print(store.product)
print(store.return_item('buty'))
print(store.product)