# 조합 함수 구현
def combination(arr, n):
    result = []
    if n > len(arr):
        return arr

    elif n == 1:
        for i in arr:
            result.append(i)

    else:
        for i in range(len(arr)-n+1):
            for j in combination(arr[i+1:], n-1):
                result.append(arr[i] + j)

    return result


# 입력값 설정
L, C = map(int, input().split())
alphabet = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
alphabet.sort()

# 모음을 포함하고 자음이 2개 이상 존재하면 정렬해서 출력
for password in combination(alphabet, L):
    cnt = L
    for vowel in vowels:
        if vowel in password:
            cnt -= 1
    if cnt != L and cnt >= 2:
        print(password)
