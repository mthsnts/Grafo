from Grafo import Grafo
from dijkstar import Graph
from Dijkstra import Dijkstra

menu = 0
g = Grafo()
graph = Graph()
valor = input('É valorado?: (S ou N)')
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
            g.criaAresta(v, vz,orientado=tipo )

    elif int(menu) == 3:
        print('\n\n')
        g.printArestas()
        print('\n\n')
        g.listAdjacencia(tipo,valor)
        g.adj(valor, tipo)
        g.incidencia(tipo)

    elif int(menu) == 4:
        nodes = []
        edges = []
        nos = input('Digite o conjunto V separado por vírgula: ')
        for n in nos.split(','):
           graph.add_node(n)
        if tipo == 'S':
            e = input('Digite o conjunto e. ex: (1,2,10)')
            for edge in e.split(')'):
                edges.append(edge)
            for edge in edges:
                graph.add_edge(edge[1],edge[2],edge[3])
        elif tipo == 'N':
            e = input('Digite o conjunto e. ex: (1,2,10)')
            for edge in e.split(')'):
                edges.append(edge)
            for edge in edges:
                graph.add_edge(edge[1], edge[2], edge[3])
                graph.add_edge(edge[2], edge[1], edge[3])
        inicio = input('qual o vertice de inicio ?')
        d = Dijkstra()
        d.dijkstra(int(inicio), nodes)


    elif int(menu) == 5:
        exit()
