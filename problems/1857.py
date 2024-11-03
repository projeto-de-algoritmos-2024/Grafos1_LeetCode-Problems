
def largestPathValue(colors: str, edges: list[list[int]]) -> int:
    
    graph = {}
    
    for item in edges:
        if item[0] not in graph:
            graph[item[0]] = {
                'vizinhos': [],
                'visitado': False
            }
        if item[1] not in graph:
            graph[item[1]] = {
                'vizinhos': [],
                'visitado': False
            }
        
        graph[item[0]]['vizinhos'].append(item[1])
    
    
    
    def enqueue(queue:list ,node: int):
        queue.append(node)
        
    def dequeue(queue:list):
        return queue.pop(0)
        
    queue = []
    
    for vertex in graph:
        if graph[vertex]['visitado'] == False:
            print(f"visitando {vertex}")
            enqueue(queue,vertex)
            graph[vertex]['visitado'] = True
            
            while len(queue) > 0:
                u = dequeue(queue)
                
                for v in graph[u]['vizinhos']:
                    if graph[v]['visitado'] == False:
                        print(f"visitando {v}")
                        graph[v]['visitado'] = True
                        enqueue(queue,v)
            
        
    

largestPathValue("abaca",[[0,1],[0,2],[2,3],[3,4]])        