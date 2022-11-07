# [1] 입력값 설정
N, H = map(int, input().split())

# [1-2] 석순(left)과 종유석(right)를 순서대로 받아 list에 저장
left = [0]*H
right = [0]*H
for n in range(N):
    if n%2:
        right[int(input())-1] += 1
    else:
        left[int(input())-1] += 1

# [2] 입력받은 데이터 가공
# [2-1] 두 list에서 오른쪽부터 왼쪽으로 숫자를 더해주면 각 줄에서의 실질적인 장애물 수가 된다.
for i in range(H-2, -1, -1):
    left[i] += left[i+1]
    right[i] += right[i+1]

# [2-2] 석순(left)와 종유석(right)를 합한 total에서 장애물의 최솟값을 찾는다.
right = right[::-1]

# 최솟값을 찾는 반복문
minV = N
cnt = 0
for i in range(H):
    obstacle = left[i] + right[i] # left와 right의 값을 합쳐 최솟값을 찾는다.
    # 최솟값이 갱신된다면 cnt 또한 1로 초기화
    if minV > obstacle:
        minV = obstacle
        cnt = 1
    # 최솟값인 경우가 복수라면 cnt + 1
    elif minV == obstacle:
        cnt += 1

print(minV, cnt)