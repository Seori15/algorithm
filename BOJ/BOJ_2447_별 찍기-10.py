# counting_stars 재귀함수 정의
def counting_stars(k):

# 재귀 종료값. k=1일 때 3x3의 arr 생성
    if k == 1:
        global arr
        arr = [['*'] * 3 for i in range(3)]
        arr[1][1] = ' '

# 이전 값을 옆으로 x3, 2번 extend
# 전체를 9칸으로 봤을 때 가운데 칸 비워주기
    else:
        len_prev = (3 ** (k - 1))     # counting_stars(k-1)의 len
        len_pre_prev = (3 ** (k - 2)) # counting_stars(k-2)의 len

        counting_stars(k-1)
        for i in range(len_prev):
            arr[i] *= 3

        for i in range(2):
            for j in range(len_prev):
                arr.extend([arr[j][:]])

        for i in range(len_prev, 2*len_prev):
            for j in range(len_prev, 2*len_prev):
                arr[i][j] = ' '

    return arr

# 입력값 설정. N에 대한 k값을 구한다.
N = int(input())
for i in range(1, 8):
    if N == 3 ** i:
        k = i
        break

# 출력값 설정
counting_stars(k)
for i in range(N):
    for j in arr[i]:
        print(j, end = '')
    print()