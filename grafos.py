#!/usr/bin/env python
# -*- coding: Latin1 -*-
import sys
class Grafo:
	def __init__(self, nome, tipo, numVertices, rotuloVertices, matriz):
		self.nome = nome
		self.numVertices = numVertices
		self.rotuloVertices = rotuloVertices
		self.tipo = tipo
		#self.matriz = matriz
		self.matriz = map(lambda x: map(lambda y: int(y), x), matriz)

	def adjacentes(self, v):
		adjs = []
		for e in range(self.numVertices):
			if self.matriz[v][e] > 0:
				adjs.append(e)
		return adjs

	
	def DFS(self):
		T = {}
		D = {}
		cor = {}
		pred = {}

		for e in range(self.numVertices):
			cor[e] = "branco"

		#v -> vertices
		#G -> grafo

		tExterno = [1]
		def loop(G, v, tempo):
			tempo+=1
			D[v] = tempo
			cor[v] = "cinza"

			for e in self.adjacentes(v):
				if cor[e] == "branco":
					pred[e] = v
					loop(G, e, tempo)
			
			cor[v] = "preto"
			tExterno[0] += tempo
			tempo+=1
			T[v] = tempo


		loop(self.matriz, 0, 0)
		return pred, T

	def BFS(self):
		G = self.matriz
		v = 0
		Q = [v] #Q -> fila
		D = [v] #D -> descobertos
		
		while len(Q) > 0:
			v = Q.pop(0)

			for w in self.adjacentes(v):
				if w not in D:
					Q.append(w)
					D.append(w)

		return D

	
	def bellmanFord(self):
		source = 0
		distance = {}
		predecessor = {}

		#passo 1: inicializar o grafo
		for v in range(len(self.matriz)):
			if v == source:
				distance[v] = 0
			else:
				distance[v] = float('inf')
			predecessor[v] = None

		#passo2: relaxamento
		for i in range(self.numVertices):
			for j in self.adjacentes(i):
				peso = self.matriz[i][j]
				if distance[i] + peso < distance[j]:
					distance[j] = distance[i] + peso
					predecessor[j] = i

		#passo3:
		for i in range(self.numVertices):
			for j in self.adjacentes(i):
				peso = self.matriz[i][j]
				if distance[i] + peso < distance[j]:
					raise Exception("Graph contains a negative-weight cycle")
		return distance, predecessor

	def noIncomingEdges(self):
		noInc = []
		for i in range(self.numVertices):
			inc = True
			for j in range(self.numVertices):
				if (i != j):
					if self.matriz[j][i] == 1:
						inc = False
			if inc:
				noInc.append(i)

		return noInc
						
						


	def ordenacaoTopologica(self):
		L = []
		S = list(set(self.noIncomingEdges()))
		matrizBkp = self.matriz

		while len(S) > 0:
			n = S.pop(0)
			L.append(n)

			for e in self.adjacentes(n):
				self.matriz[n][e] = 0
				


	#def shortestPathGAO(self):



 
def carregarGrafo(filepath):
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
	
	return Grafo(nome, tipo, numVertices, rotulos, matriz)

g = carregarGrafo(sys.argv[1])
print(g.DFS())
print(g.BFS())

try: 
	print(g.bellmanFord())
except Exception, e:
	print(str(e))



