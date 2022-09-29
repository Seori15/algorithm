# 윤년인지 아닌지 체크하기
year = int(input())
if year % 4 == 0:
    if year % 400 == 0 or year % 100 != 0:
        print(1)
    else:
        print(0)
else:
    print(0)