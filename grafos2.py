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

def buscaEmProfundidade(matriz, rotulos):
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

    def DFS(G): #G -> grafo
        #para cada vertice do grafo
        for u in range(len(rotulos)): #u -> vertice
            cor[u] = "branco"
            pred[u] = -1

        #para cada vertice do grafo
        for u in range(len(rotulos)):
            if cor[u] == "branco":
                visita(u)

    DFS(matriz)
    print("pred", pred)
    print("cor", cor)
    print("d", d)
    print("t", t)
    print("tempo", tempo[0])

print("asd")
rotulos, matriz = load("gustavera.txt")
buscaEmProfundidade(matriz, rotulos)
