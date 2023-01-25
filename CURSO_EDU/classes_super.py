class A:
    def __init__(self, atribute_a):
        self.atribute_a = atribute_a
    
    def p_atr(self):
        print(self.atribute_a)
    
class B(A):
    def __init__(self, atribute_a, atribute_b):
        super().__init__(atribute_a)
        self.atribute_b = atribute_b
        
    def p_atr(self):
        print(self.atribute_b)
    
class C(B):
    def __init__(self, atribute_a, atribute_b, atribute_c):
        super().__init__(atribute_a, atribute_b)
        self.atribute_c = atribute_c
        
    def p_atr(self):
        print(self.atribute_c)   
        super().p_atr()
        super(B, self).p_atr()
    
# c_a = A("atribute a")
# c_a.p_atr()

# c_b = B('atribute a', 'atribute b')
# c_b.p_atr()

c_c = C('atribute_a', 'atribute b', 'atribute c')
c_c.p_atr()