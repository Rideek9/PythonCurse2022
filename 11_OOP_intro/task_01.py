class Dog:
    def __init__(self, name, coat_color, race):
        self.name = name
        self.coat_color = coat_color
        self.race = race

    def szczekaj(self):
        return f"Hau Hau"

    def merdaj(self):
        return 'merdanie'


roki = Dog('Roki','szary','sznaucer')
emi = Dog('Emi','biały', 'maltańczyk')

print(roki.name,roki.coat_color, roki.race, roki.szczekaj())
print(emi.name, emi.race, emi.coat_color, emi.merdaj())