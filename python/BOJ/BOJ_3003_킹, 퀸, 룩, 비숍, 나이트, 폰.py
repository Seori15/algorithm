# 입력값 설정
K, Q, L, B, Kn, P = map(int, input().split())

# 각 체스말을 정해진 수에서 빼고 출력
K = 1 - K
Q = 1 - Q
L = 2 - L
B = 2 - B
Kn = 2 - Kn
P = 8 - P
print(K, Q, L, B, Kn, P)