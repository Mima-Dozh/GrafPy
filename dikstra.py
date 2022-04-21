import heapq






def BFS(arr, start):
    q = []
    heapq.heappush(q, arr[start])
    used = [False] * len(arr)
    while q.size() > 0:
        pointNow = heapq.heappop(q)
        for i in range(arr[pointNow]):
            if not used[i]:
                heapq.heappush(q, arr[start])
                used[i] = True
