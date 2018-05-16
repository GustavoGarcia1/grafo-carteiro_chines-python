#Cria a matriz preenchida por zeros
def cria_matriz(numero_vertices):
    matriz = []

    for i in range(numero_vertices):
        matriz.append([0] * numero_vertices)

    return matriz

#Leituras para criacao das arestas
def ler_vertice_1():
    return int(input('Digite o primeiro vertice para a conexao: '))

def ler_vertice_2():
    return int(input('Digite o segundo vertice para a conexao: '))

def ler_valor():
    return int(input('Digite o tamanho da conexão: '))

#Criando Class do Grafo
class Grafo:
    numero_vertices = 0 #Numero de vertices no grafo
    matriz = [] #Criando lista vazia para matriz

    def __init__(self, numero_vertices): #Construtor da classe
        self.matriz = cria_matriz(numero_vertices)
        self.numero_vertices = numero_vertices

    def cria_aresta(self, linha, coluna, valor): #Metodo cria_aresta
        if (linha > self.numero_vertices or coluna > self.numero_vertices):
            print('Erro! Algum dos vertices não existe, tente novamente!') #Erro caso nao existe o vertice
        else:
            self.matriz[linha - 1][coluna - 1] = valor  #Atribui valores na matriz das conexoes
            self.matriz[coluna - 1][linha - 1] = valor

if __name__ == '__main__':

    #Declaração do grafo
    g = Grafo(int(input('Digite a quantidade de vertices do grafo: ')))

    #Criando arestas
    c_aresta = str(input('Deseja adicionar conexões? (S-SIM | N-NÃO): '))
    while (c_aresta == 'S' or c_aresta == 's'):
        g.cria_aresta(ler_vertice_1(), ler_vertice_2(), ler_valor())
        c_aresta = str(input('Deseja continuar adicionando conexões? (S-SIM | N-NAO): '))

    print(g.matriz)
