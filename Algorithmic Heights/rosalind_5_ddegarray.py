data = open('rosalind_ddeg.txt','r')

vertices, nedges = map(int, data.readline().rstrip().split())
edges = [map(int, line.rstrip().split()) for line in data]

L = []
# adjacency dict with vertices as keys, 
# lists of adjacent vertices as values 
adj = {k:[] for k in range(1,vertices+1)}
for v1, v2 in edges:
    adj[v1].append(v2)
    adj[v2].append(v1)

# degree of a vertex is the number of edges that connect to it
# BUT double degree of a vertex is the number of edges that are 
# connected to ADJACENT vertices

ddeg = {k:0 for k in adj.keys()}
for vert in adj:
    for n in adj[vert]:
        ddeg[vert] += len(adj[n]) 

for k, v in sorted(ddeg.items()):
    L.append(v)

print(' '.join(str(num) for num in L))