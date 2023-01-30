from abc import ABC, abstractclassmethod

class Person:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    

class Client(Person):
    def __init__(self, name, age, account) -> None:
        super().__init__(name, age)
        self.account = account


