#Grupo: Bruna Carina e Manuele Vitoria
#Linguagem de Programação: Python
#Estrutura de dados: Matriz de Adjacência
#Tema A: Analisador de Comunidades em Redes Sociais

#BIBLIOTECAS
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import os

try:
    matplotlib.use('TkAgg')
except Exception:
    pass

#1. Leitura do grafo a partir de um arquivo txt
def ler_grafo(caminho_arq):

    with open (caminho_arq, 'r') as f: #Abre o arquivo txt e ler as linhas
        linhas = f.read().strip().splitlines()#ler, remover linhas vazias, divide em lista de linhas

    tipo = linhas[0].strip() #ler a primeira linha para verificar se D ou ND 
    arestas = [l.split() for l in linhas [1:]]#Divide as linhas em arestas
    vertices = sorted(set(v for a in arestas for v in a))#Pega os verices, set remove repetições e sorted ordena

    grafo = Grafo(tipo, vertices)#Cria a matriz de a adjacencia

    for v1, v2 in arestas: #Percorre as arestas e as adciona na matriz
        grafo.adiciona_aresta(v1,v2)
    
    return grafo

#Iniciar grafo
class Grafo:

    def __init__(self, tipo, vertices):
        
        self.tipo = tipo #Tipo de grafo, Direcionada (D) ou Não direcionada(ND)

        self.vertices = vertices #Lista do nome dos vertices
        
        self.n = len(vertices) #Quantidade total de vertices no grafo 

        self.indice = {v: i for i, v in enumerate(vertices)}#associa nome e posição

        #Matriz de adjacencia
        self.grafo = [[0]*self.n for i in range(self.n)]#cria a matrz nxn


    #Ligando dois vertices no grafo
    def adiciona_aresta(self, u, v):
        
        i,j = self.indice[u], self.indice[v]#pega o indice dos vertices

        self.grafo[i][j] = 1 #Direcionado(marca ligação de u para v)

        if self.tipo == 'ND':
             self.grafo[j][i] = 1 #Marca a ligaçao inversa



    def mostra_matriz(self):

        print('A matriz de adjacencia é:\n')
        for linha in self.grafo:
            print(linha)

    #2. Operações Basicas Obrigatorias:

    #a. Verificar Adjacência
    def verifificar_Adjacencia (self):

        #Logica: Se self.grafo[i][j] == 1, tem aresta, ou seja é adjacente
        #Se nao, nesse caso igaul a zero, não tem aresta, logo é não adjacente
        
        print('\nVertices Adjacentes:\n')
        adjacente = False #inicializar a flag

        #Checando se é igual a 1 na tabela de matriz
        for i in range(self.n):
            for j in range(self.n):
                if self.grafo[i][j] == 1: 
                    
                    #EVITA REPETIÇÃO
                    if self.tipo == 'ND' and i > j:
                        continue

                    print(f'{self.vertices[i]} - {self.vertices[j]}')
                    adjacente = True

        if not adjacente:
            print('\nNão foi encontrado vertices adjacentes')


    #b. Calcular Grau
    #Se adjacente, grau +1
    def calcular_Grau(self, vertice):

        if vertice not in self.indice: ##Checa no dicionario criado em def init se o vertice esta no grafo
            print(f'Vertice {vertice} não encontrado no grafo.')
            return
        
        i = self.indice[vertice] #posição do indice correspondente

        grau = sum(self.grafo[i])
        #self.grafo[i] linha que representa as conexões(arestas)
        #sum() soma os 1, ou seja, os adjacentes

        print(f'O grau do vertice {vertice} é: {grau}')
        return grau


    #c. Listar vizinhos
    #Se adjacente é vizinho
    def listar_Vizinhos(self, vertice):

        if vertice not in self.indice: #Checa no dicionario criado em def init se o vertice esta no grafo
            print(f'Vertice {vertice} não encontrado no grafo.')
            return
        
        i = self.indice[vertice] #posição do indice correspondente

        #Cria uma lista com os vertices adjacentes ao vertice atual
        vizinhos = [self.vertices[j] for j in range(self.n) if self.grafo[i][j] == 1]
        
        #se 1, tem ligação, então são vizinhos
        #se 0, não tem ligação


        if vizinhos:#verifica se a lista esta vazia
            print(f'Vizinhos de {vertice}: {vizinhos}')
        else:
            print(f'O vertice {vertice} não tem vizinhos.')


    #d. Listar arestas
    def listar_Arestas(self):

        print('\nArestas do grafo:\n')

        arestas = [] #Lista para guarda as arestas

        #Percorrer a matriz
        for i in range(self.n):#linha
            for j in range(self.n):#coluna
                if self.grafo[i][j] == 1: #Adjacente, encontramos a aresta
                    if self.tipo == 'ND' and i > j: #ignorar repetição das arestas
                        continue
                    arestas.append((self.vertices[i], self.vertices[j]))

        if arestas:
            for a in arestas:
                print(a)
        else:
            print('Arestas não encontradas.')


    #4. Analisador de Comunidades em Redes Sociais, Componentes Conexos
    # Ler um grafo de amizade e encontrar todos o componentes conexos
    # Exibir o numero de comunidades encontradas, listando o nime dos membros
    def encontrar_Comunidades(self):

       #Algoritmo de Busca de Profundidade
        visitado = [False]*self.n #Inicia todos como não visitado
        comunidades = [] #Lista para armazenar as comunidades

        #Procedimento de Busca Profundidade
        def DFS(i, comu):

            visitado[i] = True #Marca como visitado
            comu.append(self.vertices[i])#Adciona a lista de comunidade o vertice atual

            for j in range (self.n):#Percorre a coluna
                #Se tem arestas, chama DFS para explorar elas
                if self.grafo[i][j] == 1 and not visitado[j]:
                    DFS(j, comu)
        
        for i in range(self.n):#Percorre todos os vertices
            if not visitado[i]:
                #Inicia uma nova lista para esta comunidade
                comu = []
                DFS(i, comu)
                #Adiciona a nova comunidade a lista de comunidades
                comunidades.append(comu)

        print('\n˙⋆✮ Analise de Comunidade ✮⋆˙\n')
        print(f'Comunidaes encontradas: {len(comunidades)}\n')#tam lista comunidade
        
        #Lista cada comunidade com um numero começando em 1, e seus membros
        for idx, c in enumerate(comunidades, 1):
            print(f'Comunidade {idx}: {c}')#c é a lista com as comunidades

        return comunidades



#3.Visualização do Grafo
def visualizacao_Grafo(G: nx.Graph, output: str = None, show: bool = True, figsize=(7,5)):
   
    #Converte a matriz em um objeto networkx.Graph e gera o grafico
    G = nx.Graph()
    
    #Adiciona os vertices
    G.add_nodes_from(grafo.vertices)

    #Adiciona as arestas
    for i in range (grafo.n):
        for j in range(i + 1, grafo.n): #evita repetição
            if grafo.grafo[i][j] == 1: #tem arestas entre os vertices
                G.add_edge(grafo.vertices[i], grafo.vertices[j])
    

    plt.figure(figsize=figsize)
    pos = nx.spring_layout(G, seed = 42, k = 0.4)

    #Faz o desenho do grafo
    nx.draw(
        G, 
        pos, #Posição
        with_labels = True, #mostra o nome dos vertices
        #Visuais
        node_color = 'lightgreen',
        node_size = 400, 
        font_size = 8, 
        font_weight = 'bold', 
        edge_color = 'black'
    )

    plt.title('Grafo - Matriz de Adjacência ND', fontsize=12)

    if output:
        plt.savefig(output, dpi=300, format='jpg', bbox_inches='tight') 
        print(f'\nImagem salva como: {output}')

    if show:
        try:
            plt.show()
        except Exception as e:
            print(f"\nNão foi possível exibir a janela do gráfico ({e})")
            print("Mas a imagem foi salva corretamente.")
   
    else:
        plt.close()


#MAIN
if __name__ == '__main__':

    #1. Ler o Grafo
    grafo = ler_grafo('grafo.txt')

    print(f'\nTipo do grafo: {grafo.tipo}')
    print('\nVertices: ', grafo.vertices)
    print()

    grafo.mostra_matriz()

    #2. Operações Obrigatorias

    #a. verificar adjacencia
    grafo.verifificar_Adjacencia()

    #b. Calcular grau
    print('\nGrau de cada vertice:\n')
    for v in grafo.vertices:
        grafo.calcular_Grau(v)

    #c. Listar vizinhos
    print()
    for v in grafo.vertices:
        grafo.listar_Vizinhos(v)

    #d. Listar arestas
    print()
    grafo.listar_Arestas()

    #3. Visualizar o Grafico
    print('\nVisualização Grafica:')
    visualizacao_Grafo(grafo, output='G_visual.jpg', show = True)

    #4. Encontrar comunidades
    grafo.encontrar_Comunidades()

    input("\nExecução concluída. Pressione ENTER para sair...")
