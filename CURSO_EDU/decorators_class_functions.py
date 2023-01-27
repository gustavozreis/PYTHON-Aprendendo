def change_speed(cls):
    def new_my_speed(self):
        return self.velocity * 50
    cls.my_speed = new_my_speed
    return cls


@change_speed
class Car:
    def __init__(self, model, velocity) -> None:
        self.model = model
        self.velocity = velocity
    
    def my_speed(self):
        return self.velocity * 20
    

my_car = Car('Focus', 20)
print(my_car.my_speed())



