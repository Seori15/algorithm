# 조합 함수 설정
def combination(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n-1):
            result.append([elem] + rest)
    return result


# 입력값 설정
import sys
N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in '_'*N]


# 각 치킨집(2)에서, 각 집(1)까지의 거리를 저장한다.
chicken_distance = []
n = 0
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_distance.append([])
            for a in range(N):
                for b in range(N):
                    if city[a][b] == 1:
                        distance = abs(a-i) + abs(b-j)
                        chicken_distance[n].append(distance)
            n += 1

# chicken_distance = [[1, 2, 2, 2],
#	 				  [2, 3, 1, 1],
#					  [6, 3, 5, 3]]    -> 행 = 집(1)  열 = 치킨집(2)

house = len(chicken_distance[0])
restaurant = len(chicken_distance)

arr = list(range(0, restaurant)) # 조합 함수 사용을 위한 리스트 [0, 1, 2]

# 조합을 사용해서 살아남을 치킨집의 경우의 수를 정한다.
# 정해진 치킨집에 대해서 각 집까지의 거리 정보를 저장한다(temp)
# 각 집에서 치킨집까지의 가장 짧은 거리를 구해서 더하고(sumV)
# 모든 조합 경우의 수에 대해서 min값을 찾는다(min(sum_list))
sum_list = []
for i in combination(arr, M):
    temp = []
    for j in i:
        temp.append(chicken_distance[j])

    sumV = 0
    for a in range(house):
        minV = 100
        for b in range(M):
            if minV > temp[b][a]:
                minV = temp[b][a]
        sumV += minV
    sum_list.append(sumV)

print(min(sum_list))