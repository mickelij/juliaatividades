class Carro:
    def __init__ (self, marca, modelo, cor, ano):
       self.marca = marca
       self.modelo = modelo
       self.cor = cor
       self.ano = ano

    def ligar (self):
       print (self.modelo, 'está ligado') 
       
    def desligar (self):
       print (self.modelo, 'está desligado') 
       
    def imprimir_info (self):
       print ('Marca: ', self.marca)
       print ('Modelo: ',self.modelo)
       print ('Cor : ',self.cor)
       print ('Ano: ',self.ano)

carro1 = Carro('selta','chevrolet','preto','2017')
carro2 = Carro('skyline','GTR','cinza','1999')

carro1. ligar() 
carro2. ligar () 

carro1.desligar()
carro2.desligar()

carro1. imprimir_info() 
carro2. imprimir_info()