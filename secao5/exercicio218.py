class carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante
        
class motor:
    def __init__(self, nome):
        self.nome = nome
        
class fabricante:
    def __init__(self, nome):
        self.nome = nome
        
        
fabricante1 = fabricante("porsche")
motor1 = motor("12 cilindros")
carro1 = carro("panamera", motor1, fabricante1)

print(carro1.fabricante.nome, carro1.nome, carro1.motor.nome)