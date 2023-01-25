class Person:
    
    __foo = 2
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.__foo = 2
        
    def test(self):
        print(self.__foo)
        
    def __private(self):
        print(2)
        
    
gustavo = Person('gustavo', 35)    
    
print(gustavo.test())

print(gustavo.__foo)