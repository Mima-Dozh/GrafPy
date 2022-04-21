from collections import deque






def BFS(arr, start):
    q = deque()
    q.append(arr[start])
    used = [False] * len(arr)
    while q.size() > 0:
        pointNow = q.pop()
        for i in range(arr[pointNow]):
            if not used[i]:
                q.append(i)
                used[i] = True
