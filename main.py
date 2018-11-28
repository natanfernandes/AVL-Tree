class Node():
    def __init__(self,val):
        self.val = val
        self.esquerda = None
        self.direita = None
        self.sucessor = None
        self.antecessor = None

class Tree():
    def __init__(self):
        self.node = None
        self.altura = 0
        self.fator_balanceamento = 0

    def getAltura(self):
        if self.node != None:
            return self.altura
        else 
            return 0

    def calcFatorBalanceamento(self):
        #fb = alturaDireita - alturaEsquerda    
        pass
    
    def rebalancear(self):
        pass
    
    def rotacionarDireita(self):
        pass

    def rotacionarEsquerda(self):
        pass

    def inserir(self,val):
        pass
    
    def deletar(self,val):
        pass

    def buscar(self,val):
        pass