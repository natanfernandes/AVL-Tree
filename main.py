class Node():
    def __init__(self,val):
        self.val = val
        self.esquerda = None
        self.direita = None

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

    def sucessor(self,node):    #retorna o sucessor, o menor valor a esquerda
        node = node.direita.node  
        if node != None: 
            while node.esquerda != None:    #procura a esquerda ate a arvore ficar vazia
                if node.esquerda.node == None: 
                    return node 
                else: 
                    node = node.esquerda.node  
        return node 

    def antecessor(self, node): #retorna o antecessor, o maior valor a direita
        node = node.esquerda.node 
        if node != None: 
            while node.direita != None:   #procura a direita ate a arvore ficar vazia
                if node.direita.node == None: 
                    return node 
                else: 
                    node = node.direita.node  
        return node 

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
        #aux1 = raiz antiga
        #aux2 = filho a esquerda da raiz antiga
        #aux3 = filho a direita do filho a esquerda
        aux1 = self.node 
        aux2 = self.node.esquerda.node
        aux3 = aux2.direita.node 
        
        self.node = aux2 #nova raiz
        aux2.direita.node = aux1  #raiz original vira filho a direita da nova raiz
        aux1.esquerda.node = aux3   #vira filho da esquerda do filho a direita


    def rotacionarEsquerda(self):
        #aux1 = raiz antiga
        #aux2 = filho a direita da raiz antiga
        #aux3 = filho a esquerda do filho a direita
        aux1 = self.node 
        aux2 = self.node.direita.node 
        aux3 = aux2.esquerda.node 
        
        self.node = aux2 #nova raiz
        aux2.esquerda.node = aux1 #raiz original vira filho a esquerda da nova raiz
        aux1.direita.node = aux3 #vira filho da direita do filho a esquerda

    def inserir(self,val):
        tree = self.node
        
        newNode = Node(val)
        
        if tree == None:
            self.node = newNode 
            self.node.esquerda = Tree() 
            self.node.direita = Tree()
            print("inseriu : ", val )
        
        elif val < tree.val: 
            #se valor que tentar inserir for menor, ele chama o metodo dnv para a esquerda
            self.node.esquerda.inserir(val) 
            
        elif val > tree.val: 
            #se valor que tentar inserir for maior, ele chama o metodo dnv para a direita
            self.node.direita.inserir(val)
        
        else: 
            print(val, " ja esta na arvore")
            
        self.rebalancear() 
    
    def deletar(self,val):
        if self.node != None: 
            if self.node.val == val: 
                if self.node.esquerda.node == None and self.node.direita.node == None:
                    self.node = None 
               
                # deleta todos os filhos da sub-arvore
                # caso ache a esquerda ou a direita 
                elif self.node.esquerda.node == None: 
                    self.node = self.node.direita.node
                elif self.node.direita.node == None: 
                    self.node = self.node.esquerda.node
                
                # caso tenha filho tanto a esquerda quanto a direita
                # ele acha um sucessor e faz a troca entre os valores 
                # e chama o metodo para excluir o filho a direita
                else:  
                    aux = self.sucessor(self.node)
                    if aux != None:   
                        self.node.val = aux.val 
                        self.node.direita.deletar(aux.val)
                    
                self.rebalancear()
                return  
            elif val < self.node.val: 
                self.node.esquerda.deletar(val)  
            elif val > self.node.val: 
                self.node.direita.deletar(val)
                        
            self.rebalancear()
        else: 
            return 

    def buscar(self,val):
        if self.node != None:
            if self.node.val == val:
                print('Achado o valor : ',val)
            elif val < self.node.val: 
                self.node.esquerda.buscar(val)  
            elif val > self.node.val: 
                self.node.direita.buscar(val)
        else:
            print('Nao esta na arvore')

    def print(self,level=0, pref=''):
        self.calcTamanho()
        if(level == 0):
            pref = "(Raiz)"
       
        self.calcFatorBalanceamento()
        if(self.node != None): 
            print ('Nivel : ',str(level), pref,' Valor do No : ', self.node.val, "[ Altura = " + str(self.altura) + " : FB = " + str(self.fator_balanceamento) + "]", 'Folha' if self.e_folha() else ' ')   
            if self.node.esquerda != None: 
                self.node.esquerda.print(level + 1, '<')
            if self.node.esquerda != None:
                self.node.direita.print(level + 1, '>')

if __name__ == "__main__": 
    tree = Tree()
    tree.inserir(1)
    tree.inserir(5)
    tree.inserir(89)
    tree.inserir(96)
    tree.inserir(2)
    tree.inserir(4)
    
    tree.print()
    tree.deletar(96)
    tree.print()
    tree.buscar(4)