# 유효성 검증 함수 설정
# board[n]이 가장 최근에 둔 퀸이다. 이 퀸이 앞서 두었던 퀸들과 행이 겹치거나, 대각선에 위치한다면 False를 return한다.
def gn(n):
    for i in range(n):
        if board[n] == board[i] or abs(board[n] - board[i]) == abs(n - i):
            return False

    return True


# Queen을 두는 함수 설정
def queen(n):
    global ans
    # 종료 조건. N개의 Queen을 둘 수 있으면 1을 반환
    if n == N:
        ans += 1
        return

    # 2차원 체스판을 1차원 리스트로 축약하여 푼다.
    # 1차원 리스트의 각 원소는 체스판에서의 n번 열을 의미한다.
    # 1열(n=0)부터 순서대로 n행에 퀸을 둔다.
    for i in range(N):
        board[n] = i
        # 방금 둔 퀸이 조건상 가능한 위치라면, 재귀한다.
        if gn(n):
            queen(n+1)


# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [0]*N
    ans = 0
    queen(0)
    print(f'#{test_case} {ans}')


ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 함수 하나만 쓰는 방법
# Queen을 두는 함수 설정
def queen(n):
    global ans
    # 종료 조건. N개의 Queen을 둘 수 있으면 ans +1 적립
    if n == N + 1:
        ans += 1
        return

    # 2차원 체스판을 1차원 리스트로 축약하여 푼다.
    # 1차원 리스트의 각 원소는 체스판에서의 n번 열을 의미한다.
    # 1열(n=1)부터 순서대로 n행에 퀸을 둔다.
    for i in range(1, N + 1):
        board[n] = i

        # 유효성 검증
        # 앞서 둔 퀸들과 범위가 겹친다면 break, 그렇지 않다면 재귀한다.
        for j in range(1, n):
            if board[n] == board[j] or abs(board[n] - board[j]) == abs(n - j):
                board[n] = 0
                break
        else:
            queen(n + 1)
            board[n] = 0


# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [0] * (N + 1)
    ans = 0
    queen(1)
    print(f'#{test_case} {ans}')