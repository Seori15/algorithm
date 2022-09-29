# 입력값 설정하기
arr = list(input())

# 출력을 위한 arr2 설정하여 arr의 원소를 순서대로 넣어줌.
arr2 = []
for i in range(len(arr)):
    try:
        int(arr[i])
        arr2.append(arr[i])

# 산수 기호가 나타나면 2번 pop하여 계산 후 넣어줌.
    except ValueError:
        b = int(arr2.pop())
        a = int(arr2.pop())
        if arr[i] == '+':
            arr2.append(a + b)
        if arr[i] == '-':
            arr2.append(a - b)
        if arr[i] == '*':
            arr2.append(a * b)
        if arr[i] == '/':
            arr2.append(a / b)

print(int(arr2[-1]))