# 입력값 설정하기
H, W = map(int, input().split())
arr = list(map(int, input().split()))

# 왼쪽부터 오른쪽으로, start보다 숫자가 크거나 같은 지점이 나올 때 arr[start] - arr[j]만큼 더함.
i = 0
start = 0
rainism = 0
while i < W:
    if arr[i] >= arr[start]:
        for j in range(start, i):
            rainism += arr[start] - arr[j]
        start = i
    i += 1

# 오른쪽부터 왼쪽으로, end보다 숫자가 큰 지점이 나올 때 arr[end] - arr[j]만큼 더함.
i = W-1
end = W-1
while i >= 0:
    if arr[i] > arr[end]:
        for j in range(end, i, -1):
            rainism += arr[end] - arr[j]
        end = i
    i += -1

print(rainism)