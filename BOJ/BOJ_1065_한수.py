# 한수의 개수 출력하기
N = int(input())
result = 0
for i in range(1, N+1):
    if i <= 99:
        result += 1
    elif i <= 999:
        i = str(i)
        for j in range(len(i)-2):
            if int(i[j]) - int(i[j+1]) == int(i[j+1]) - int(i[j+2]):
                result += 1

print(result)