class Student:
    unieversity = 'New York Univerity'
    min_avg = 4.5
    uni_code = "UAM"

    def __init__(self,first,last,age,avg):
        self.first = first
        self.last = last
        self.age = age
        self.avg = avg

    def __repr__(self):
        return f'{self.first.capitalize()} {self.last.capitalize()} średnia : {str(self.avg)}'

    def mail(self):
        return f'{self.last.lower()}.{self.first.lower()}@{self.uni_code.lower()}.com'

    def grant_scholarship(self):
        if self.avg >- self.min_avg:
            print("Gratulacje, stypendium przyznane")
        else:
            print("Niestety stypendium nie zostało przyznane")

    @classmethod
    def change_name_university(cls,name_university):
        cls.uni_code = name_university



obj_anna = Student('Anna','Krawczyk',25,4.5)
obj_adam = Student('Adam', 'Maślak' ,28,3.5)
obj_anna.change_name_university('opa')
print(obj_anna.mail())
print(obj_adam.mail())