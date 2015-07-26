def load(filepath):
    f = open(filepath, 'r')

    nome= f.readline().replace("\n|\r", "")
    tipo = int(f.readline().replace("\n|\r", ""))
    numVertices = int(f.readline().replace("\n|\r", ""))
    rotulos = []

    for _ in range(numVertices):
        rotulos.append(f.readline().replace("\n|\r", ""))

    matriz = []

    for _ in range(numVertices):
        matriz.append(f.readline().replace("\r\n", "").split())

    return rotulos, matriz



def adjacente(G, v):
    adj = []
    for e in range(len(G[v])):
        if G[e] > 0:
            adj.append(e)

    return adj

def DFS(matriz, rotulos):
    pred = {}
    cor = {}
    d = {}
    t = {}
    tempo = [0]

    def visita(u): #u -> vertice
        cor[u] = "cinza"
        tempo[0] += 1
        d[u] = tempo
        for v in adjacente(matriz, u):
            if cor[v] == "branco":
                pred[v] = u
                visita(v)

        cor[u] = 'preto'
        tempo[0] += 1
        t[u] = tempo

    #para cada vertice do grafo
    for u in range(len(rotulos)): #u -> vertice
        cor[u] = "branco"
        pred[u] = -1

    #para cada vertice do grafo
    for u in range(len(rotulos)):
        if cor[u] == "branco":
            visita(u)

    #print("pred", pred)
    #print("cor", cor)
    #print("d", d)
    #print("t", t)
    #print("tempo", tempo[0])
    return pred

def BFS(matriz, rotulos):
    cor = {}
    antecessor = {}
    d = {}
    Q = []

    def innerBFS(s):
        Q.append(s)

        #enquanto a fila Q for vazia
        while len(Q) > 0:
            u = Q.pop(0)
            for v in adjacente(matriz, u):
                if cor[v] == "branco":
                    cor[v] = "cinza"
                    d[v] = d[u] + 1
                    antecessor[v] = u
                    Q.append(v)
            cor[u] = "preto"

    for u in range(len(rotulos)):
        cor[u] = "branco"
        d[u] = float('inf')
        antecessor[u] = None

    for u in range(len(rotulos)):
        if cor[u] == "branco":
            innerBFS(u)

    print("cor", cor)
    print("antecessor", antecessor)
    print("d", d)
    print("Q", Q)

def relaxamento(matriz, rotulos):
    predecessor = {}
    distance = {}
    #passo2: relaxamento
    for i in range(len(rotulos)):
        for j in adjacente(matriz, i)
            peso = matriz[i][j]
            if distance[i]  + peso < distance[j]:
                distance[j] = distance[i] + peso
                predecessor[j] = i
    return predecessor, distance



def bellmanFord(matriz, rotulos, s):
    source = s
    distance = {}
    predecessor = {}

    #passo1: inicializar o grafo
    for v in range(len(rotulos)):
        if v == source:
            distance[v] = 0
        else:
            distance[v] = float('inf')
        predecessor[v] = None

    #passo2: relaxamento
    '''
    for i in range(len(rotulos)):
        for j in adjacente(matriz, i)
            peso = matriz[i][j]
            if distance[i]  + peso < distance[j]:
                distance[j] = distance[i] + peso
                predecessor[j] = i
    '''
    predecessor, distance = relaxamento(matriz, rotulos)

    #passo3
    for i in range(len(rotulos)):
        for j in adjacente(matriz, i):
            peso = matriz.[i][j]
            if distance[i] + peso < distance[j]:
                raise Exception("Graph contains a negative-weight cycle")

    return predecessor

def caminhoMaisCurtoGao(matriz, rotulos, s):
    dist = {}
    predecessor = DFS(matriz, rotulos)


    #inicializar origem unica
    dist[s] = 0
    for e in predecessor:
        if e != s:
            predecessor[e] = -1
            dist[e] = float("inf")

    #relaxamento
    predecessor, distancia = relaxamento(matriz, rotulos)

#s->no inicial
def removeMenor(l):
    min = 0
    for e in range(len(l)):
        if l[min] > l[e]:
            min = e

    return l.pop(min)

def prim(matriz, rotulos, s):
    custo = {}
    p = {}

    for u in range(len(rotulos)):
        custo[u] = float('inf')
        p[u] = None

    custo[s] = 0
    Q = range(len(rotulos))

    while (len(Q) > 0):
        u = removeMenor(Q)
        for v in adjacente(G, u):
            if (v in Q) and matriz[u][v] < custo[v]:
                p[v] = u
                custo[v] = matriz[u][v]

rotulos, matriz = load("gustavera.txt")
DFS(matriz, rotulos)
BFS(matriz, rotulos)
bellmanFord(matriz, rotulos, 0)
