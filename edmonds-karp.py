MAXN = 10
INF = 2147483646

def bfs(s, t,check) :
	parent = [-1 for i in range(MAXN)]
	path_flow = [0 for i in range(MAXN)]
	q=[s]
	parent[s] = -2
	path_flow[s] = INF

	while(q):
		u = q.pop(0)
		for i in range(len(graph[u])) :	
			v = graph[u][i]
			if(parent[v] == -1):
				if(capacity[u][v] - flowPassed[u][v] >0):
					parent[v] = u
					path_flow[v] = min(path_flow[u], capacity[u][v]- flowPassed[u][v])
					if(v == t):
						if(check==True):return path_flow[t]
						else: return parent

					q.append(v)  
	return 0

def max_flow(source,sink):
	maxFlow = 0 
	while(True):
		flow = bfs(source,sink,True)
		parent=bfs(source,sink,False)
		if(flow == 0):
			break
		u = sink
		maxFlow += flow
		while (u!=source):
			v = parent[u]
			flowPassed[v][u] += flow
			flowPassed[u][v] -+ flow
			u=v
	return maxFlow

n=int(input())
e=int(input())
s=int(input())
t=int(input())
capacity = [[0]*n for i in range(e)]
graph = [[0]*n for i in range(e)]
flowPassed = [[0]*n for i in range(e)]
for i in range(0,e) :
	inp=str(input())
	inp=list(map(int,inp.split()))
	From=inp[0]
	to=inp[1]
	cap=inp[2]
	capacity[From][to]=cap
	graph[From].append(to)
	graph[to].append(From)
maxFlow = max_flow(s,t)
print(maxFlow)
