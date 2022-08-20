# 뒤집은 값 비교하기
s1, s2 = input().split()
s1, s2 = s1[::-1], s2[::-1]
print(max(s1, s2))