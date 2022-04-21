used = {} 
def DFS(a, start):
    used[start] = True
    for i in range(a[start]):
        if not used.ContainsKey(i):
            DFS(a, i)