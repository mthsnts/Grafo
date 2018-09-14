class Vertice:

    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = list()


    def setVizinho(self, vizinho):
        if vizinho not in self.vizinhos :
            self.vizinhos.append(vizinho)
            # self.vizinhos.sort()

    def getVizinho(self):
        print( self.nome,self.vizinhos)