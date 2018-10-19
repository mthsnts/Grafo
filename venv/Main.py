from Grafo import Grafo
from dijkstar import Graph, find_path


class Dijkstra:

    def getdijkstra(self, x, node, graph):

        cost_func = lambda u, v, e, prev_e: e['cost']
        for n in node:
            if n is not x:
                print(find_path(graph, x, n, cost_func=cost_func))


menu = 0
g = Grafo()
d = Dijkstra()
graph = Graph()
valor = 'S'
tipo = input('É orientado? (S ou N)')
while int(menu) < 5:
    menu = input('\n\n--------------------------------\n'
                 '1 - insereir vertice\n'
                 '2 - inserir conjunto v\n'
                 '3 - Mostrar formas de representação\n'
                 '4 - Dijkstra'
                 '5- Sair'
                 '-> ')
    if int(menu) == 1:
        nome = input('Digite o conjunto V separado por vírgula: ')
        for n in nome.split(','):
            g.newVertice(n)
    elif int(menu) == 2:
        v = input('nome do vertice: ')
        vz = input('nome do vizinho: ')

        if valor.lower() == 's':
            vl = input('qual o valor da aresta ?')
            g.criaAresta(v, vz, valor.lower(), vl, tipo)
        elif valor.lower() == 'n':
            g.criaAresta(v, vz, orientado=tipo)

    elif int(menu) == 3:
        print('\n\n')
        g.printArestas()
        print('\n\n')
        g.listAdjacencia(tipo, valor)
        g.adj(valor, tipo)
        g.incidencia(tipo)

    elif int(menu) == 4:
        nodes = []
        edges = []
        nos = input('Digite o conjunto V separado por vírgula,(Apenas números): ')
        for n in nos.split(','):
            nodes.append(int(n))
            graph.add_node(int(n))
        if tipo == 'S':
            q = 'S'
            while q == 'S':
                q = input('Deseja inserir aresta ?')
                if q == 'S':
                    v1 = input('digite vertice 1:   ')
                    v2 = input('digite vertice 2:   ')
                    vl = input('digite o valor:     ')

                    graph.add_edge(int(v1), int(v2), {'cost': int(vl)})

        elif tipo == 'N':
            q = 'S'
            while q == 'S':
                q = input('Deseja inserir aresta ?(S/N)')
                if q == 'S':
                    v1 = input('digite vertice 1:   ')
                    v2 = input('digite vertice 2:   ')
                    vl = input('digite o valor:     ')

                    graph.add_edge(int(v1), int(v2), {'cost': int(vl)})
                    graph.add_edge(int(v2), int(v1), {'cost': int(vl)})
        inicio = input('qual o vertice de inicio ?')
        print(nodes)
        d.getdijkstra(int(inicio), nodes, graph)

    elif int(menu) == 5:
        exit()
