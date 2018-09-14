from Grafo import Grafo

menu = 0
g = Grafo()
valor = input('É valorado?: (S ou N)')
tipo = input('É orientado? (S ou N)')
while int(menu) < 5:
    menu = input('\n\n--------------------------------\n'
                 '1 - insereir vertice\n'
                 '2 - inserir conjunto v\n'
                 '3 - Mostrar formas de representação\n'
                 '4- Sair'
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
        exit()
