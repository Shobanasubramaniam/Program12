IN = 9999
MAX = 10
def dijkstra(graph,n,start_node):
    cost = [[IN]* n for _ in range(n)]
    distance = [IN]*n
    pred = [-1]*n
    visited=[False]*n
    for i in range(n):
        for j in range(n):
            if graph[i][j] = 0:
                cost[i][j] = IN
            else:
                cost[i][j] = graph[i][j]
    for i in range(n):
        distance[i] = cost[start_node][i]
        pred[i] = start_node
    distance[start_node]=0
    visited[start_node]= True
    count=1
    while count<n:
        min_dis = IN
        next_node = None
        for i in range(n):
            if not visited[i] and distance[i]<min_dis:
                min_dis = distance[i]
                next_node =i
            if next_node is None:
                break
            visited[next_node]=True
            for i in range(n):
                if not visited[i]:
                    new_distance = min_dis+ cost[next_node][i]

                if next_distance