# [1] 입력값 설정
s1 = input()
s2 = input()
L1 = len(s1)
L2 = len(s2)

# [2] DP 풀이. L1 X L2의 dp 배열을 만들어서 겹치는 값을 센다.
dp = [[0] * L2 for _ in range(L1)]
for i in range(L1):
    for j in range(L2):
        # [2-1] s1과 s2의 문자열이 겹치는 (i, j)칸에 숫자를 표기한다.
        # (i-1, j-1)칸의 +1을 표기하면 연속되는 문자열의 길이를 나타낸다.
        if s1[i] == s2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1

# [3] dp 배열에서 max값 출력
print(max(map(max, dp)))