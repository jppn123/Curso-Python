from random import randint
class Pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self, frase):
        
        return print(f"oi eu sou {self.nome}, {frase}")
    
    
    @classmethod 
    def porAnoNascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod #n precisa de self ou cls
    def gerar_id():
        return randint(2, 22222)
    
    #getter
    @property
    def nome(self):
        return self._nome
    #setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    