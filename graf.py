import bfs

if __name__ == '__main__':
    print("Введите количество вершин")
    g = [[] for i in range(int(input()))]
    print("Ведите количество ребер")
    n = int(input())
    for i in range(n):
        f, s = map(int, input().split())
        g[f].append(s)