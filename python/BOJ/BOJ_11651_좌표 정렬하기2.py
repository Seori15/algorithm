# 입력값 설정
N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

# 람다함수 활용하여 2번 정렬
arr.sort(key = lambda x : (x[1], x[0]))

for i in range(N):
    print(*arr[i])