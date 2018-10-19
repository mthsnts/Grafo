from dijkstar import Graph, find_path

class Dijkstra:

    graph = Graph()
    graph.add_edge(1, 2, {'cost': 1})
    graph.add_edge(2, 3, {'cost': 2})

    def getdijkstra(x, graph,nodeList):
        cost_func = lambda u, v, e, prev_e: e['cost']
        for n in nodeList:
            if n is not x:
                print(find_path(graph, x, n, cost_func=cost_func))


graph = Graph()
graph.add_edge(1, 2, {'cost': 1})
graph.add_edge(2, 3, {'cost': 2})
n = [1,2,3]
Dijkstra.getdijkstra(1,graph,n)