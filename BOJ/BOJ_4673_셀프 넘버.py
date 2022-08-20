# 생성자 n의 d(n)을 구하는 함수 작성
def d(n):
    y = n
    n = str(n)
    for i in range(len(n)):
        y += int(n[i])
    return y

# 셀프 넘버 출력하기
your_number = []
for i in range(10000):
    your_number.append(d(i))
    if i not in your_number:
        print(i)