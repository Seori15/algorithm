# [a] 궁수의 공격 대상을 찾는 target 함수 설정
def target(n):
    minV = 100
    target = 0
    for enemy in enemies2:
        distance = abs(enemy[0] - N) + abs(enemy[1] - n)
        if distance <= D and minV >= distance:
            minV = distance
            target = enemy
    if target:
        return target
    return False

# [b] target을 공격하는 attack 함수 설정
def attack(i):
    global kill
    archer = archers[i]
    target1 = target(archer[0]) # [a]
    target2 = target(archer[1])
    target3 = target(archer[2])

    # 각 궁수의 target 중복체크
    if target1:
        enemies2.remove(target1)
        kill += 1
    if target2 and target2 != target1:
        enemies2.remove(target2)
        kill += 1
    if target3 and target3 != target1 and target3 != target2:
        enemies2.remove(target3)
        kill += 1

# [c] 적이 이동하는 move 함수 설정
def move(enemies2):
    moved_enemies = []
    for [a, b] in enemies2:
        if a == N-1:
            pass
        else:
            moved_enemies.append([a+1, b])

    return moved_enemies

# [1] 입력값 설정
from sys import stdin
N, M, D = map(int, stdin.readline().split())
arr = [[] for _ in '_'*N]
for i in range(N):
    arr[i] = list(map(int, stdin.readline().split()))

# [2] 적의 좌표값 저장
enemies = []
for j in range(M-1, -1, -1):
    for i in range(N):
        if arr[i][j] == 1:
            enemies.append([i, j])

# [3] 궁수 배치의 경우의 수를 조합으로 구현
from itertools import combinations
lst = list(range(M))
archers = list(combinations(lst, 3))


# [4] 모든 궁수 배치마다의 경우의 수를 반복함.
result = 0
for i in range(len(archers)):
    kill = 0
    enemies2 = enemies[:] # 적의 제거 수와 적 배치를 그 때마다 초기화

    # 적이 남아있다면, 궁수 공격 후 이동한다.
    while enemies2:
        attack(i) # [b]
        enemies2 = move(enemies2)[:] # [c]
    if result < kill:
        result = kill

print(result)