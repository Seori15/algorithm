# 입력값 설정
N = int(input())
words = list({input() for i in range(N)})

# 람다함수로 2번 정렬
words.sort(key = lambda x : (len(x), x))
for word in words:
    print(word)