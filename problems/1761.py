class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        
        matriz = []
        
        for i in range(n):
            linha = [False] * n
            matriz.append(linha)