# 입력값 설정하기
King, Stone, N = input().split()
King = list(King)
Stone = list(Stone)
King_x = ord(King[0])
King_y = int(King[1])
Stone_x = ord(Stone[0])
Stone_y = int(Stone[1])
N = int(N)

# King의 이동 방향에 따른 dx, dy 설정
direction = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

# 조건에 따라 King과 Stone이 이동
for i in range(N):
    move = input()
    for j in range(len(direction)):
        if direction[j] == move:
            x = King_x + dx[j]
            y = King_y + dy[j]
            if x < 65 or x > 72 or y < 1 or y > 8:
                continue
            elif x == Stone_x and y == Stone_y:
                sx = Stone_x + dx[j]
                sy = Stone_y + dy[j]
                if sx < 65 or sx > 72 or sy < 1 or sy > 8:
                    continue
                else:
                    Stone_x, Stone_y = sx, sy
                    King_x, King_y = x, y
            else:
                King_x, King_y = x, y

ax = chr(King_x)
ay = str(King_y)
bx = chr(Stone_x)
by = str(Stone_y)
print(ax + ay)
print(bx + by)
