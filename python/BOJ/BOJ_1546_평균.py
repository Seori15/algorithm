# 평균값 조작하기
N = int(input())
scores = list(map(int, input().split()))
print(sum(scores) / N * 100 / max(scores))