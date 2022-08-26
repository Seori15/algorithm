# 입력값 설정
A, B, V = map(int, input().split())

n = (V-A) // (A-B) + 1
if (V-A)%(A-B):
    n += 1
print(n)