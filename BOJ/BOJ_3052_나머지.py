# 나머지 계산 후 중복값 제거하기
A = []
for i in range(10):
    A.append(int(input()) % 42)
print(len(set(A)))