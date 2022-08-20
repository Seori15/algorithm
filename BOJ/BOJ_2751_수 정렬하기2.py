# 입력값 설정하기
N = int(input())
arr = ['']*2000001

# arr에서 해당하는 index에 값을 입력 후 순서대로 출력
for i in range(N):
    n = int(input())
    arr[n+1000000] = n

for i in arr:
    if i != '':
        print(i)