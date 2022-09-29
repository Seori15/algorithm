# 0-1. 가위바위보로 승자를 가리는 win 함수
def win(i, j):
    if arr[i] == arr[j]:
        return i
    elif (arr[i] - arr[j]) % 3 == 1:
        return i
    else:
        return j

# 0-2. 토너먼트 그룹을 나누는 group 함수
def group(i, j):
    if i == j:
        return i
    else:
        left = group(i, (i+j)//2)
        right = group((i+j)//2 +1, j)
        return win(left, right)

# 1. 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

# 2. 양식에 맞게 출력하기
    result = group(0, N-1)
    print(f'#{test_case} {result + 1}')