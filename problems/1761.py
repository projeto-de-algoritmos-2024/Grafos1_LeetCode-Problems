class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        
        matriz = []
        
        for i in range(n):
            linha = [False] * n
            matriz.append(linha)
            
        graus =  n * [0]
        
        for u, v in edges:
            matriz[u][v] = True
            matriz[v][u] = True
            graus[u] += 1
            graus[v] += 1
            
        grau_minimo = float('inf')
        
        for u in range(n):
            for v in range(n):
                if matriz[u][v]:
                    for w in range(n):
                        if matriz[u][w] and matriz[v][w]:
                            grau_trio = graus[u] + graus[v] + graus[w] - 6
                            grau_minimo = min(grau_minimo, grau_trio)
                            
        if grau_minimo == float('inf'):
            return -1
        else:
            return grau_minimo
            
            