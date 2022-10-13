'''
arr2의 원소들과 추의 무게 n을 더한 plus, 차이인 minus를 arr에 추가하면서,
만약 구슬의 무게만큼의 결과가 나왔다면 result를 'Y'로 바꿔준다.
마지막에는 추의 무게인 n을 arr에 추가하면서 result를 비교한다.
'''
# [A] 각 원소의 합과 차를 찾아주는 f 함수 설정
def f(arr2, n):
    for i in arr2:
        # [A-1] 각 원소와 추의 무게를 더한 plus
        plus = i+n
        arr.add(plus)
        if bead[plus]:
            result[bead[plus]-1] = 'Y'
        # [A-2] 각 원소와 추의 무게를 뺀 minus
        minus = abs(i-n)
        arr.add(minus)
        if bead[minus]:
            result[bead[minus]-1] = 'Y'
    # [A-3] 추의 무게 n
    arr.add(n)
    if bead[n]:
        result[bead[n] - 1] = 'Y'


# [1] 입력값 설정
from sys import stdin
N = int(stdin.readline())
weight = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
beads = list(map(int, stdin.readline().split()))

# [1-1] 무게가 n인 구슬의 bead[n]에 index값을 저장한다.
bead = [0]*40001
for i in range(M):
    bead[beads[i]] = i+1

# [2] f 함수로 구슬의 무게를 잴 수 있는지 확인
result = ['N']*M
arr = set()
for i in weight:
    arr2 = arr.copy()
    f(arr2, i)

print(*result)