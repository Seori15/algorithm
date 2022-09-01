# 입력값 설정
N = int(input())
arr = [int(input()) for _ in range(N)]

# index 함수 사용하기 위해 arr을 뒤집음
arr = arr[::-1]
cnt = 0

# ilbunnam이 유일하게 가장 큰 값일 때, cnt를 출력
while True:
    ilbunnam = arr[-1]
    if ilbunnam == max(arr) and arr.count(ilbunnam) == 1:
        print(cnt)
        break
    else:
        arr[arr.index(max(arr))] += -1
        arr[-1] += 1
        cnt += 1
