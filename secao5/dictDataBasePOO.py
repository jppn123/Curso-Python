class BaseDeDados:
    def __init__(self):
        self.dados = dict()
        
    def inserir_cliente(self, id, nome):
        
        if "clientes" not in self.dados:
            self.dados["clientes"] = {id:nome}
            
        else:
           self.dados["clientes"].update({id:nome})
       
        
    def lista_clientes(self):
        for id, nome in self.dados["clientes"].items():
            print(id, nome)
            
    def deletar_cliente(self, id):
        del self.dados["clientes"][id]
        
  
bd = BaseDeDados()
bd.inserir_cliente(1, "joao")
bd.inserir_cliente(2,"cal")
bd.inserir_cliente(3, "alex")
bd.inserir_cliente(4, "adddlex")
bd.deletar_cliente(2)
bd.lista_clientes()
