# Para usar
```
	python grafos.py [caminho do arquivo] [argumentos]
```

# Argumentos:
* nenhum argumento -> imprime todos
* all -> imprime todos
* prim -> algoritmo de prim
* bfs -> algoritmo breadth first search
* dfs -> algoritm depth first search
* gao -> caminho mais curto

***obs: Caso o seu algoritmo tenha um **source** (aresta inicial), ele será a primeira aresta***

# Arquivo exemplo:
## Especificação
´´´
	NOME_DO_MAPA
	TIPO_DO_GRAFO(1,2) *desprezível no momento
	8 -> quantidade de arestas
	a }
	b }}
	c }}}
	d }}}}
	e }}}}}}}} arestas
	f }}}}
	g }}}
	h }
	0 0 0 1 1 0 0 0  }
	0 0 0 1 0 0 0 0  }}
	0 0 0 0 1 0 0 1  }}}
	0 0 0 0 0 1 1 1  }}}} Grafo
	0 0 0 0 0 0 1 0  }}}
	0 0 0 0 0 0 0 0  }}
	0 0 0 0 0 0 0 0  }
```

## Exemplo
```
	MAPA1
	2
	8
	a
	b
	c
	d
	e
	f
	g
	h
	0 0 0 1 1 0 0 0
	0 0 0 1 0 0 0 0
	0 0 0 0 1 0 0 1
	0 0 0 0 0 1 1 1
	0 0 0 0 0 0 1 0
	0 0 0 0 0 0 0 0
	0 0 0 0 0 0 0 0
```
