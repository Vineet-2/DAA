import math

def bellmon_ford(v,edges,src):
    dist=[math.inf for i in range(v)]
    dist[src]=0

    for i in range(v-1):
        for j in edges:
            u=j[0]
            v=j[1]
            wt=j[2]

            if v==src:
                continue
            elif (dist[u] != math.inf and dist[u] + wt < dist[v]):
                dist[v] = dist[u] + wt
    
    for j in edges:
        u=j[0]
        v=j[1]
        wt=j[2]

        if (dist[u] != math.inf and dist[u] + wt < dist[v]):
            return [-1 for i in range(v)], False

    return dist,True

v=int(input("Enter the No. of Vertices-> "))
edges=[]
print(f"Name of Vertices Should be between 0 and {v-1}")
while True:
    edge=[]
    edge.append(int(input("Enter the First Vertice-> ")))
    edge.append(int(input("Enter the Second Vertice-> ")))
    edge.append(int(input("Enter the Weight Between the Edges-> ")))
    edges.append(edge)

    ch=str(input("Do You Want to add more edges y/n-> "))
    if ch=="n":
        break

src=int(input("Enter the Source Node-> "))

dist,flag = bellmon_ford(v,edges,src)

if flag==False:
    print("Negative Cycle Present")
else:
    print("Final Distance from Source Node: ",dist)