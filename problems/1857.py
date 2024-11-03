import pprint
def largestPathValue(colors: str, edges: list[list[int]]) -> int:
    
    colors_cont = {}
    
    for i in colors:
        if i not in colors_cont:
            colors_cont[i] = 0
        
    
    graph = {}
    
    for item in edges:
        if item[0] not in graph:
            
            graph[item[0]] = {
                'vizinhos': [],
                'visitado': False,
                'cor': colors[item[0]]
            }
        if item[1] not in graph:
            
            graph[item[1]] = {
                'vizinhos': [],
                'visitado': False,
                'cor': colors[item[1]]
            }
        
        graph[item[0]]['vizinhos'].append(item[1])
    
    
    
    def enqueue(queue:list ,node: int):
        queue.append(node)
        
    def dequeue(queue:list):
        return queue.pop(0)
        
    queue = []
    
    for vertex in graph:
        if graph[vertex]['visitado'] == False:
        
            enqueue(queue,vertex)
            graph[vertex]['visitado'] = True
            colors_cont[graph[vertex]['cor']]+=1
            
            while len(queue) > 0:
                u = dequeue(queue)
                
                for v in graph[u]['vizinhos']: 
                    if graph[v]['visitado'] == False:
                        graph[v]['visitado'] = True
                        colors_cont[graph[v]['cor']]+=1
                        enqueue(queue,v)
         
    return colors_cont[max(colors_cont, key=colors_cont.get)]
    

largestPathValue("abaca",[[0,1],[0,2],[2,3],[3,4]])        