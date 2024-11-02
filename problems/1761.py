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
            
            