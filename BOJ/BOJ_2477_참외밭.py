# 입력값 설정
import sys
K = int(sys.stdin.readline())

arr = []        # 밭 길이의 값만을 담는 리스트
arr2 = [[],[]]  # 밭 길이를 세로, 가로로 나눈 리스트
for i in range(6):
    a, b = map(int, sys.stdin.readline().split())

    if a == 1 or a == 2:
        arr2[0].append(b)
    elif a == 3 or a == 4:
        arr2[1].append(b)
    arr.append(b)

# arr2에서 max를 통해 width와 height를 구할 수 있다.
width = max(arr2[1])
height = max(arr2[0])
Square = width * height

# 반시계 방향으로 돌 때 width 다음 height값이 나오지 않는다면, 튀어나온 부분이다.
# 이 경우 arr 내에서 width 다음 2번째, 3번째 값이 작은 네모의 가로 세로값이다.
# width 다음 height가 맞다면 width 다음 3번째, 4번째 값이 작은 네모다.
# IndexError 방지를 위해 arr을 2배로 늘리고서 계산한다.
arr *= 2
if arr[arr.index(width)+1] != height:
    square = arr[arr.index(width)+2] * arr[arr.index(width)+3]
else:
    square = arr[arr.index(width)+3] * arr[arr.index(width)+4]

Area = Square - square
print(K * Area)