# dfs 함수 설정
def dfs(x, y, n, num):
    # 종료조건1. 범위를 벗어남
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return

    num += arr[x][y]
    # 종료조건2. 7자리 숫자가 채워짐
    if n == 7:
        nums.add(num)
        return

    dfs(x+1, y, n+1, num)
    dfs(x-1, y, n+1, num)
    dfs(x, y+1, n+1, num)
    dfs(x, y-1, n+1, num)

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    arr = [list(input().split()) for _ in '_'*4]
    nums = set()
    num = ''
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, num)

    print(f'#{test_case} {len(nums)}')
