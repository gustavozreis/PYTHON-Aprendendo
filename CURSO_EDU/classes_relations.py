# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name) -> None:
       self.name = name
       self._motor = None
       self._brand = None
       
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, value):
        self._motor = value
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value
        
    def car_specs(self):
        print(self.name, ' | ', self._motor.name, ' | ', self._brand.name)


class Motor:
    def __init__(self, name) -> None:
        self.name = name        
        
class Brand:
    def __init__(self, name):
        self.name = name
        
        
chevrolet = Brand('Chevrolet')
v8 = Motor('V8')

ford = Brand('Ford')
motor_v12 = Motor('V12')

camaro = Car('Camaro')
camaro.brand = chevrolet
camaro.motor = v8

ferrari = Car('Ferrari')
ferrari.motor = motor_v12
ferrari._brand = ford

help(Car)

        
