from abc import ABC, abstractmethod

class Grafo(ABC):
    
    @abstractmethod
    def numero_de_vertices(self):
        pass
    
    @abstractmethod
    def numero_de_arestas(self):
        pass
    
    @abstractmethod
    def sequencia_de_graus(self):
        pass
    
    @abstractmethod
    def adicionar_aresta(self):
        pass
    
    @abstractmethod
    def remover_aresta(self):
        pass
    
    @abstractmethod
    def imprimir(self):
        pass
