

class Dog:
    biology_class = 'Animals'  #static class - not changed all in this class are animals

    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed

    def run(self):
        return 'I can run'

    def get_name(self):
        return f'Hello! My name is {self.name}!'


dog1 = Dog('Pula', '8', 'Jack Russel Terrier')
print(dog1.name)
print(dog1.get_name())
print(dog1)
print(dog1.breed)
print(dog1.biology_class)

dog2 = Dog('Kira', '10', 'French Bulldog')
print(dog2.get_name())
print(dog2.biology_class)


#наследование класса

class Corgi(Dog):
    def __init__(self, name, weight, breed, passport):  #новый атрибут паспорт можем добавить
        super().__init__(name, weight, breed)
        self.passport = passport

    def give_a_paw(self):
        return 'I can give a paw'

    def run(self):
        return 'I can run fast!'


dog3 = Corgi('Dana', 12, 'Corgi', 'Type1')
# print(dog3.get_name())
# print(dog3.biology_class)
# print(dog3.give_a_paw())
# print(dog3.passport)

# print(dog2.passport)

print(dog2.run())
print(dog3.run())     #same method with different implementation

