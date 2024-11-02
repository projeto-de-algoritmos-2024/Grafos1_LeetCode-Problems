class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visitado = [False] * n
        
        def dfs(cidade):
            visitado[cidade] = True
            for vizinha in range(n):
                if isConnected[cidade][vizinha] == 1 and not visitado[vizinha]:
                    dfs(vizinha)
                    
        provincias = 0
        
        for i in range(n):
            if not visitado[i]:
                dfs(i) 
                provincias += 1

        return provincias
