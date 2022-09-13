# 전위, 중위, 후위 순회 함수 설정
def pre(str):
    if str in par:
        print(str, end= '')
        pre(chL[par.index(str)])
        pre(chR[par.index(str)])

def inorder(str):
    if str in par:
        inorder(chL[par.index(str)])
        print(str, end= '')
        inorder(chR[par.index(str)])

def post(str):
    if str in par:
        post(chL[par.index(str)])
        post(chR[par.index(str)])
        print(str, end= '')

# 입력값 설정
V = int(input())
par = [0] * V
chL = [0] * V
chR = [0] * V

for i in range(V):
    par[i], chL[i], chR[i] = input().split()

pre('A')
print()
inorder('A')
print()
post('A')