from pessoa import Pessoa

c1 = Pessoa("jp", 19)
c2 = Pessoa.porAnoNascimento("joao", 2004)

print(c1.nome,"tem",c1.idade)
print(c2.nome,"tem",c2.idade)

c1.nome