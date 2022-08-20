# N번의 별 우측 정렬하여 출력하기
N = int(input())
for i in range(1, N+1):
    stars = i*'*'
    print(stars.rjust(N))