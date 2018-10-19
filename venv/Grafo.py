from Vertice import Vertice
from itertools import groupby


class Grafo:
    vertices = []
    arestas = []
    valores = []

    def newVertice(self, nome):  # cria um novo vertice
        for vt in self.vertices:
            if vt.nome == nome:
                print('Esse vértice já existe')
                return False
        else:
            v = Vertice(nome)
            self.vertices.append(v)

    def criaAresta(self, vertice, vizinho, valor='n', vl=0, orientado='s'):
        vtc = ''
        vz = ''
        self.valores.append(vl)
        for v in self.vertices:
            if v.nome == vertice:
                vtc = v.nome
                v.setVizinho(vizinho)

        for v in self.vertices:
            if v.nome == vizinho and vtc != '':
                vz = vizinho

        if valor != 's':
            self.arestas.append((vtc, vz))
            print(self.arestas)
        if orientado == 'n' and valor == 'n':
            for v in self.vertices:
                if v.nome == vizinho:
                    v.setVizinho(vtc)
            self.arestas.append((vz, vtc))
            print(self.arestas)

        elif valor == 's' and orientado == 'n':
            self.arestas.append((vtc, vz, vl))
            self.arestas.append((vz, vtc, vl))
            self.arestaAux.append((vtc,vz,vl))
            print(self.arestas)
        elif valor == 's' and orientado == 's':
            self.arestas.append((vtc, vz, vl))

    def printArestas(self, orientado='s'):
        print('lista de Arestas[', end='')

        for aresta in self.arestas:
            if orientado == 's':
                print(aresta, end=',')
            elif orientado == 'n':
                print(aresta, end=',')
                print([t[::-1] for t in aresta], end=',')
        print(']')

    def listAdjacencia(self, orientado='n', valorado='n'):
        print('Lista de adjacencia\n')
        if orientado == 'n' and valorado == 'n':
            for vertice in self.vertices:
                vertice.getVizinho()
        elif orientado == 's' and valorado == 'n':
            for vertice in self.vertices:
                vertice.getVizinho()
        # adj = {k: [v[1] for v in g] for k, g in groupby(sorted(self.arestas), lambda e: e[0])}
        # print(adj)

    def adj(self, val='n', orientado='s'):
        print('------matriz adjacencia-----\n')
        if val == 'n' and orientado == 'n':
            for vertice in self.vertices:
                print(vertice.nome.upper(), end=' ')
            print('\n')
            for v1 in self.vertices:
                for v2 in self.vertices:
                    if (v1.nome, v2.nome) in self.arestas:
                        print(1, end=' ')
                    elif (v2.nome, v1.nome) in self.arestas:
                        print(1, end=' ')
                    elif (v1.nome, v2.nome) not in self.arestas:
                        print(0, end=' ')
                print(v1.nome.upper())
                print()
        elif val == 's' and orientado == 's':
            for vertice in self.vertices:
                print(vertice.nome.upper(), end='  ')
            print('\n')
            for v1 in self.vertices:
                for v2 in self.vertices:
                    res = [tup[2] for tup in self.arestas if tup[0] == v1.nome and tup[1] == v2.nome]
                    if res != []:
                        print(res[0], end='  ')
                    elif res == []:
                        print(0, end='  ')
                print('\n')
        elif val == 'n' and orientado == 's':
            for vertice in self.vertices:
                print(vertice.nome.upper(), end=' ')
            print('\n')
            for v1 in self.vertices:
                for v2 in self.vertices:
                    if (v1.nome, v2.nome) in self.arestas:
                        print(1, end=' ')
                    elif (v1.nome, v2.nome) not in self.arestas:
                        print(0, end=' ')
                print(v1.nome.upper())
                print()
        elif val == 's' and orientado == 'n':
            for vertice in self.vertices:
                print(vertice.nome.upper(), end='  ')
            print('\n')
            for v1 in self.vertices:
                for v2 in self.vertices:
                    res = [tup[2] for tup in self.arestas if tup[0] == v1.nome and tup[1] == v2.nome]
                    if res != []:
                        print(res[0], end='  ')
                    elif res == []:
                        print(0, end='  ')
                print('\n')

    def incidencia(self, orientado):
      if orientado == 'n':
        rmvdbl = ''
        print('MATRIZ DE INCIDENCIA\n')
        for aresta in self.arestas:
            if aresta[2] != rmvdbl:
                print(aresta[2], end='  ')
                rmvdbl = aresta[2]
        print('\n')
        for vertice in self.vertices:
            for aresta in self.arestaAux:
                if aresta[0] == vertice.nome or aresta[1] == vertice.nome:
                    print(1, end='  ')
                else:
                    print(0,end='  ')
            print(vertice.nome.upper())
            print('\n')
      elif orientado == 's':
          print('MATRIZ DE INCIDENCIA\n')
          for aresta in self.arestas:
                  print(aresta[2], end='  ')
          print('\n')
          for vertice in self.vertices:
              for aresta in self.arestas:
                  if aresta[0] == vertice.nome:
                      print(1, end='  ')
                  elif aresta[1] == vertice.nome:
                      print('-1', end='  ')
                  else:
                      print(0, end='  ')
              print(vertice.nome.upper())
              print('\n')
