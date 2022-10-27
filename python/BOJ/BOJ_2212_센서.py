# [1] 입력값 설정
N = int(input())
K = int(input())

# [1-1] N개의 센서를 lst에 담고 내림차순으로 정렬하자.
lst = list(map(int, input().split()))
lst.sort(reverse=True)

# [2] 조건 설정
# [2-1] N이 1일 때를 상정하지 않으면 100%에서 IndexError가 발생한다.
if N == 1:
    result = 0

# [2-2] 이 문제는 전체 길이에서 센서 사이의 거리가 큰 경우를 K-1번만큼 빼주면 된다.
else:
    # [2-3] lst2에 정렬된 센서간의 거리를 담고, 내림차순으로 정렬한다.
    lst2 = []
    for i in range(N-1):
        lst2.append(lst[i]-lst[i+1])

    lst2.sort(reverse=True)

    # [2-4] result를 전체 길이로 설정해두고, K-1번만큼 lst2 앞의 값을 빼준다.
    result = lst[0] - lst[-1]

    n = 0
    for i in range(K-1):
        result -= lst2[n]
        n += 1

print(result)
