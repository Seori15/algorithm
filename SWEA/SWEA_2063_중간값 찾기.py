# list 정렬하여 중간값 찾기
N = int(input())
list = list(map(int, input().split()))
list.sort()

for i in range(N):
    if i == ((N-1)/2):
        print(list[i])
        break