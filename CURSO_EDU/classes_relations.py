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
    def __init__(self, name, motor) -> None:
        self.name = name
        self.motor = motor
        
    def add_motor(self, motor):
        self.motor = motor


class Motor:
    def __init__(self, name) -> None:
        self.name = name
        
        
class Brand:
    def __init__(self, name):
        self.name = name
    
    def build_car(self, car):
        self.car = car
        
    def car_spec(self):
        print(self.name, '|', self.car.name, '|', self.car.motor.name)
        
        
motor_v8 = Motor('Motor V8')

camaro = Car('Camaro', motor_v8)
# camaro.add_motor(motor_v8)
print(camaro.motor.name)


chevrolet = Brand('Chevrolet')
chevrolet.build_car(camaro)

print(chevrolet.name,',', chevrolet.car.name,',', chevrolet.car.motor.name)
print()

chevrolet.car_spec()
        
