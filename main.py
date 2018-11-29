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
        else: 
            return 0

    def calcFatorBalanceamento(self, recursivo = True):
        #fb = alturaDireita - alturaEsquerda    
        if not self.node == None: 
            if recursivo:  #enquanto recursivo, ele chama o metodo até chegar num no vazio e seta o fb = 0
                if self.node.esquerda != None: 
                    self.node.esquerda.calcFatorBalanceamento()
                if self.node.direita != None:
                    self.node.direita.calcFatorBalanceamento()

            self.fator_balanceamento = self.node.esquerda.altura - self.node.direita.altura 
        else: 
            self.fator_balanceamento = 0 

    def calcTamanho(self, recursivo = True):
        if not self.node == None: 
            if recursivo: #enquanto recursivo, ele chama o metdo até chegar num no vazio e seta sua altura = -1
                if self.node.esquerda != None: 
                    self.node.esquerda.calcTamanho()
                if self.node.direita != None:
                    self.node.direita.calcTamanho()
            
            self.altura = max(self.node.esquerda.altura,self.node.direita.altura) + 1 
        else: 
            self.altura = -1


    def e_folha(self):
        if self.altura == 0:
            return True
        else: 
            return False

    

    def rebalancear(self):
        # checando se a arvore está balanceada e a rebalenceando
        self.calcTamanho(False)
        self.calcFatorBalanceamento(False)
        while self.fator_balanceamento < -1 or self.fator_balanceamento > 1: 
            if self.fator_balanceamento > 1:    
                if self.node.esquerda.fator_balanceamento < 0:  #se o fb > 1 e o fb do no < 0 ele roda para esquerda 
                    self.node.esquerda.rotacionarEsquerda() 
                    self.calcTamanho()
                    self.calcFatorBalanceamento()
                self.rotacionarDireita()        #se o fb nao for < 0 ele roda para direita
                self.calcTamanho()
                self.calcFatorBalanceamento()
                
            if self.fator_balanceamento < -1:
                if self.node.direita.fator_balanceamento > 0:  #se o fb < -1 e o fb do no > 0 ele roda para direita
                    self.node.direita.rotacionarDireita()
                    self.calcTamanho()
                    self.calcFatorBalanceamento()
                self.rotacionarEsquerda()         #se o fb nao for > 0 ele roda para esquerda
                self.calcTamanho()
                self.calcFatorBalanceamento()

    
    def rotacionarDireita(self):
        aux1 = self.node #guardando o no atual
        aux2 = self.node.esquerda.node #guardando o no a esquerda
        aux3 = aux2.direita.node #guardando o no a direita do que esta a esquerda do atual
        
        self.node = aux2
        aux2.direita.node = aux1
        aux1.esquerda.node = aux3


    def rotacionarEsquerda(self):
        aux1 = self.node 
        aux2 = self.node.direita.node 
        aux3 = aux2.esquerda.node 
        
        self.node = aux2 
        aux2.esquerda.node = aux1 
        aux1.direita.node = aux3

    def inserir(self,val):
        tree = self.node
        
        newnode = Node(val)
        
        if tree == None:
            self.node = newnode 
            self.node.esquerda = Tree() 
            self.node.direita = Tree()
            print("inseriu : ", val )
        
        elif val < tree.val: 
            self.node.esquerda.inserir(val)
            
        elif val > tree.val: 
            self.node.direita.inserir(val)
        
        else: 
            print(val, " ja esta na arvore")
            
        self.rebalancear() 
    
    def deletar(self,val):
        pass

    def buscar(self,val):
        pass

if __name__ == "__main__": 
    tree = Tree()
    tree.inserir(1)
    tree.inserir(5)
    tree.inserir(89)
    tree.inserir(4)
    tree.inserir(1)
    print(tree.node)