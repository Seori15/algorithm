# [1] 입력값 설정
N, K = map(int, input().split())
nums = list(map(int, input()))
ans = []

# [2] nums의 숫자를 앞에서 하나씩 ans에 append한다.
#     앞자리 숫자가 큰게 핵심이므로 비교하면서 pop한다.
for num in nums:
   while K != 0 and ans and ans[-1] < num:
       ans.pop()
       K -= 1
   ans.append(num)

# [3] 54321 혹은 1111과 같은 반례들이 있다면 [2]에서 K가 0이 되지 않을 수 있다.
while K != 0:
    ans.pop()
    K -= 1
print(''.join(map(str, ans)))