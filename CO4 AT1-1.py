# Atchaya Vharsne S (192524185)
def prims(graph):
  n=len(graph)
  visited=[False]*n
  visited[0]=True
  cost=0
  for k in range(n-1):
    minimum=float('inf')
    x=y=-1
    for i in range(n):
      if visited[i]:
        for j in range(n):
          if not visited[j] and graph[i][j]!=0:
            if graph[i][j]<minimum:
              minimum=graph[i][j]
              x=i
              y=j
    visited[y]=True
    cost+=minimum
  return cost
graph=[[0,2,3],[2,0,1],[3,1,0]]
print(prims(graph))
  
