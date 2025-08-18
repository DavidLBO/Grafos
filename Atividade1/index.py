from GrafoDenso import GrafoDenso

# Criando grafo com rótulos
g = GrafoDenso(["A", "B", "C", "D", "E"])

# Adicionando arestas
g.adicionar_aresta("A", "B")
g.adicionar_aresta("A", "C")
g.adicionar_aresta("C", "D")
g.adicionar_aresta("C", "E")
g.adicionar_aresta("B", "D")

print("=== Grafo Original ===")
g.imprimir()
print("Número de vértices:", g.numero_de_vertices())
print("Número de arestas:", g.numero_de_arestas())
print("Sequência de graus:", g.sequencia_de_graus())

# Removendo aresta (A, C)
g.remover_aresta("A", "C")

print("\n=== Após remover aresta (A, C) ===")
g.imprimir()
print("Número de vértices:", g.numero_de_vertices())
print("Número de arestas:", g.numero_de_arestas())
print("Sequência de graus:", g.sequencia_de_graus())
