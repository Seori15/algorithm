# 가위바위보에 따른 결과값 설정하기
a, b = input().split()
a = int(a)
b = int(b)

if a == 1:
    if b == 2:
        print("B")
    elif b == 3:
        print("A")

elif a == 2:
    if b == 1:
        print("A")
    if b == 3:
        print("B")

elif a == 3:
    if b == 1:
        print("B")
    if b == 2:
        print("A")