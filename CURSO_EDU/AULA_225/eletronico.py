from log import LogFileMixin

class Eletronic:
    def __init__(self, name) -> None:
        self.name = name
        self._power = False
        
    def turn_on(self):
        if not self._power:
            self._power = True
        
    def turn_off(self):
        if self._power:
            self._power = False
        

class Smartphone(Eletronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()
        
        if self._power:
            msg = f'{self.name} está ligado.'
            self.log_success(msg)
            
    def turn_off(self):
        super().turn_off()
        
        if not self._power:
            msg = f'{self.name} está desligado'
            self.log_error(msg)
        
        
        