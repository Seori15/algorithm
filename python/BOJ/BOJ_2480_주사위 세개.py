# 주사위 수에 따라 상금 출력하기
a, b, c = map(int, input().split())
check = set([a, b, c])

if len(check) == 1:
    print(1000 * a + 10000)
elif len(check) == 3:
    print(max(a, b, c) * 100)
else:
    if a == b or a == c:
        print(a * 100 + 1000)
    else:
        print(b * 100 + 1000)