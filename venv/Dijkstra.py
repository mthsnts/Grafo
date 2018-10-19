from dijkstar import Graph, find_path


# graph = Graph()
# graph.add_edge(1, 2, {'cost': 1})
# graph.add_edge(2, 3, {'cost': 2})
# graph.add_edge(3, 1, {'cost': 10})
# graph.add_edge(1, 4, {'cost': 2})
#
# nos = [1,2,3,4]

class Dijkstra:

    def dijkstra(x=2, nodeList=None):
        cost_func = lambda u, v, e, prev_e: e['cost']
        for n in nodeList:
            if n is not x:
                print(find_path(graph, x, n, cost_func=cost_func))


dijkstra()

# from Grafo import Grafo
#
# def Dijkstra(Grafo, source):
#     for vertice in Grafo.vertices:
#         dist[vertice.nome] = 'infinito'
#         previous[vertice.nome] = None
#     dist[source] = 0
#     Q[] = Grafo.nodes
#     while sizeof(Q) != 0:
#         u = min(Q)
#         Q.pop(u)
#         for v in u.previous
#             alt = dist[u] + dist_between(u,v)
#             if alt < dist[v]
#                 dist[v] = alt
#                 previous[v] = u
#     return previous[]
