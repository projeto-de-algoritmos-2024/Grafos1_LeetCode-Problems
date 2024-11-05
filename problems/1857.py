from collections import defaultdict
def largestPathValue(colors: str, edges: list[list[int]]) -> int:
    
    if len(list) == 0:
        return 1
    
    num_nos = len(colors)
    nos_sem_chegada = set()
    for i in range(num_nos):
        nos_sem_chegada.add(i)
        
    grafo = defaultdict(set)
    grau_entrada = defaultdict(int)
    
    for origem, destino in edges:
        grafo[origem].add(destino)
        grau_entrada[destino] += 1
        nos_sem_chegada -= {destino}
    
    maximo_caminho = -1
    caminho_cor = defaultdict(dict)

    for raiz in nos_sem_chegada:
        grau_entrada[raiz] = 0
        caminho_cor[raiz][colors[raiz]] = 1
        fila = [raiz]
        
        while fila:
            atual = fila.pop(0)
            
            for vizinho in grafo[atual]:
                grau_entrada[vizinho] -= 1
                if grau_entrada[vizinho] == -1: 
                    return -1
                for cor in caminho_cor[atual]:
                    caminho_cor[vizinho].setdefault(cor, caminho_cor[atual][cor])
                    caminho_cor[vizinho][cor] = max(caminho_cor[vizinho][cor], caminho_cor[atual][cor])
                if grau_entrada[vizinho] == 0:
                    fila.append(vizinho)
                    cor_vizinho = colors[vizinho]
                    caminho_cor[vizinho].setdefault(cor_vizinho, 0)
                    caminho_cor[vizinho][cor_vizinho] += 1
                    maximo_caminho = max(maximo_caminho, caminho_cor[vizinho][cor_vizinho])

    return maximo_caminho
        
    

largestPathValue("hhqhuqhqff",[[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]])        