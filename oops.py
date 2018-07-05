class Dog():

    kind = 'canine'
    def __init__(self, name, color):
        self.name = name
        self.age = 0



    def bark(self):
         print(self.name, 'is barking')


d1 = Dog('tommy','brown')

print(d1.name)