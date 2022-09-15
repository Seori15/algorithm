# 입력값 설정
import sys
from itertools import product
arr = [list(map(int, sys.stdin.readline().split())) for i in range(5)]

# 이동 방향을 위한 delta 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = [0, 1, 2, 3] # 상 하 좌 우

words_list = []  # 완성된 6자리 숫자가 저장될 list
for i in range(5): # 익숙한 2중 for문 탐색으로 25가지 수를 읽음.
    for j in range(5):

        # 중복순열 product. 4**5의 1024개 경우의수를 불러옴.
        # 이제 이 1024가지 경우의 수를 1개씩 pop하면서 다 돌거임.
        pro = list(product(direction, repeat=5))
        while len(pro) != 0:
            a, b = i, j
            words = str(arr[a][b]) # words에 현위치 숫자를 저장.

            # 1개씩 pop하는데, (a, b) 좌표가 범위를 넘어가면 그냥 break해버림.
            # 범위 안에서 6자리 숫자를 완성하면 words_list에 추가
            for n in pro.pop(0):
                if 0 <= a + dx[n] < 5 and 0 <= b + dy[n] < 5:
                    a += dx[n]
                    b += dy[n]
                    words += str(arr[a][b])
                    if words not in words_list and len(words) == 6:
                        words_list.append(words)
                else:
                    break

print(len(words_list))