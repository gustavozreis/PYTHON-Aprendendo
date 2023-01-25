class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.height = None
        
    def set_height(self, height):
        self.height = height
        

gustavo = Person('Gustavo', 32)
print(gustavo.height)

gustavo.set_height(170)

print(gustavo.height)