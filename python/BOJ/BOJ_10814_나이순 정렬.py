# 입력값 설정
import sys
N = int(sys.stdin.readline())
members = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

# 람다함수로 1번 정렬
members.sort(key = lambda x : x[0])
for member in members:
    print(*member)