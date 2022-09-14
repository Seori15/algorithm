# 입력값 설정
import sys
n, w, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# index를 포함하는 trucks 리스트 생성
trucks = [() for _ in '_'*n]
for i in range(n):
    trucks[i] = (i, arr[i])

bridge = []
time = [0]*n
weight = 0
result = 0
while len(trucks) != 0:
    a, b = trucks.pop(0) # a는 index, b는 트럭 무게

    if weight + b > L:                # 만약 하중을 초과한다면
        while weight + b > L:         # 맨 앞 트럭이 빠질때까지 시간을 진행시킨다.
            rest = time[bridge[0][0]]
            result += w-rest          # 진행 시간을 result에 저장
            for index, truck in bridge[::-1]:
                time[index] += w-rest
                if time[index] == w:
                    weight -= truck
                    bridge.pop(0)

    weight += b                       # 트럭이 다리에 오른다
    bridge.append((a, b))
    result += 1
    for index, truck in bridge[::-1]: # 시간을 1 단위시간 진행시킨다.
        time[index] += 1
        if time[index] == w:
            weight -= truck
            bridge.pop(0)

rest = time[-1]
result += w+1-rest  # while문 조건상 마지막 트럭이 올라가면 끝나므로 나머지를 더한다.
print(result)