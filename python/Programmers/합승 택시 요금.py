# n = 6
# s = 4
# a = 6
# b = 2
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 0], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n = 6
s = 4
a = 5
b = 6
fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]

def dijkstra(start):
    for _ in '_'*n:
        maxV = INF
        for i in range(1, n+1):
            if maxV > key[i] and not visited[i]:
                maxV = key[i]
                now = i

        visited[now] = 1

        for i in range(1, n+1):
            if adjM[now][i] and not visited[i]:
                key[i] = min(key[i], key[now] + adjM[now][i])

    return key[s] + key[a] + key[b]

adjM = [[0]*(n+1) for _ in '_'*(n+1)]
for c, d, f in fares:
    adjM[c][d] = f
    adjM[d][c] = f


INF = 100001*n
result = INF
for i in range(1, n+1):
    visited = [0]*(n+1)
    key = [INF]*(n+1)
    key[i] = 0
    result = min(result, dijkstra(i))

print(result)