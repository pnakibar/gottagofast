#!/usr/bin/env python
# -*- coding: Latin1 -*-
import sys

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
        matriz.append(map(lambda x: int(x), f.readline().replace("\r\n", "").split()))

    return rotulos, matriz



def adjacente(G, v):
    adj = []
    for e in range(len(G[v])):
        if G[v][e] > 0:
            adj.append(e)

    return adj

def DFS(matriz, rotulos, ordtop=False):
    pred = {}
    cor = {}
    d = {}
    t = {}
    tempo = [0]
    LISTA_ORDENACAO_TOPOLOGICA = []

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
        LISTA_ORDENACAO_TOPOLOGICA.append(u)

    #para cada vertice do grafo
    for u in range(len(rotulos)): #u -> vertice
        cor[u] = "branco"
        pred[u] = -1

    #para cada vertice do grafo
    for u in range(len(rotulos)):
        if cor[u] == "branco":
            visita(u)

    '''
    print("pred", pred)
    print("cor", cor)
    print("d", d)
    print("t", t)
    print("tempo", tempo[0])
    '''
    if ordtop:
        return LISTA_ORDENACAO_TOPOLOGICA
    else:
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

    d[range(len(rotulos))[0]] = 0 #coloca o primeiro com peso 0
    for u in range(len(rotulos)):
        if cor[u] == "branco":
            innerBFS(u)
    '''
    print("cor", cor)
    print("antecessor", antecessor)
    print("d", d)
    print("Q", Q)
    '''
    return antecessor


def relaxamento(matriz, rotulos, distance):
    predecessor = {}
    #passo2: relaxamento
    for i in range(len(rotulos)):
        for j in adjacente(matriz, i):
            peso = int(matriz[i][j])

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
        for j in adjacente(matriz, i):
            peso = matriz[i][j]
            if distance[i]  + peso < distance[j]:
                distance[j] = distance[i] + peso
                predecessor[j] = i
    '''
    predecessor, distance = relaxamento(matriz, rotulos, distance)

    #passo3
    for i in range(len(rotulos)):
        for j in adjacente(matriz, i):
            peso = matriz[i][j]
            if distance[i] + peso < distance[j]:
                raise Exception("Graph contains a negative-weight cycle")

    return predecessor


def caminhoMaisCurtoGao(matriz, rotulos, s):
    d = {}
    lot = DFS(matriz, rotulos, ordtop=True) #TODO: ordenar pelo valor
    predecessor = {}

    #inicializar origem unica
    for v in range(len(rotulos)):
        predecessor[v] = None
        d[v] = float("inf")
    d[s] = 0

    #relaxamento
    print("lot", lot)
    for u in lot:
        print("u:", str(u), "adjacente: ", adjacente(matriz,u))
        for v in adjacente(matriz, u):
            if d[v] > d[u] + matriz[u][v]:
                d[v] = d[u] + matriz[u][v]
                predecessor[v] = u

    print("predecessor", predecessor)
    print("d", d)


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
        for v in adjacente(matriz, u):
            if (v in Q) and matriz[u][v] < custo[v]:
                p[v] = u
                custo[v] = matriz[u][v]
    print(custo)
    print(p)


rotulos, matriz = load(sys.argv[1])
'''
print("dfs:")
print(DFS(matriz, rotulos))
print("bfs:")
print(BFS(matriz, rotulos))
print("bellmanFord:")
print(bellmanFord(matriz, rotulos, 0))
'''
print("caminhoMaisCurtoGao")
print(caminhoMaisCurtoGao(matriz, rotulos, 0))
'''
print("prim")
print(prim(matriz, rotulos, 0))
'''
