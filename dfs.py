used = {} 
ans = []
def DFS(a, start):
    print(used)
    used[start] = True
    for i in a[start]:
        if not used.get(i):
            DFS(a, i)
    ans.append(start)

def topological_sort(a):
    used.clear()
    for i in range(len(a)):
        if not used.get(i):
            DFS(a, i)
    return ans[::-1]
