from Grafo import Grafo

class GrafoDenso(Grafo):

    def __init__(self, vertices):
        if isinstance(vertices, int):
            self.rotulos = list(range(vertices))
        elif isinstance(vertices, list):
            self.rotulos = vertices
        else:
            raise ValueError("Parâmetro 'vertices' deve ser int ou lista.")

        self.num_vertices = len(self.rotulos)
        self.matriz = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        self.arestas = 0

    def numero_de_vertices(self):
        return self.num_vertices

    def numero_de_arestas(self):
        return self.arestas

    def sequencia_de_graus(self):
        return [sum(self.matriz[i]) for i in range(self.num_vertices)]

    def adicionar_aresta(self, u, v):
        i, j = self.rotulos.index(u), self.rotulos.index(v)
        if self.matriz[i][j] == 0:  
            self.matriz[i][j] = 1
            self.matriz[j][i] = 1  
            self.arestas += 1

    def remover_aresta(self, u, v):
        i, j = self.rotulos.index(u), self.rotulos.index(v)
        if self.matriz[i][j] == 1:
            self.matriz[i][j] = 0
            self.matriz[j][i] = 0
            self.arestas -= 1

    def imprimir(self):
        print("   " + " ".join(map(str, self.rotulos)))
        for idx, linha in enumerate(self.matriz):
            print(f"{self.rotulos[idx]}: " + " ".join(map(str, linha)))