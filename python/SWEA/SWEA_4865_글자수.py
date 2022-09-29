# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    str1 = set(input())				# 중복값 제거를 위해 set 설정
    str2 = input()

# str1의 원소가 str2의 원소와 같을 때 cnt +1하여 최대값 출력
    result = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if result <= cnt:
            result = cnt
    print(f'#{test_case} {result}')