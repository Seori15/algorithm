def solution(play_time, adv_time, logs):

    # [A] 시간을 숫자로 바꿔주는 함수
    def to_int(time):
        hh, mm, ss = time.split(':')
        return (int(hh) * 3600 + int(mm) * 60 + int(ss))

    # [B] 숫자를 시간으로 바꿔주는 함수
    def to_time(int):
        ss = str(int % 60)
        tmp = int // 60
        mm = str(tmp % 60)
        hh = str(tmp // 60)

        ss = '0' + ss if len(ss) == 1 else ss
        mm = '0' + mm if len(mm) == 1 else mm
        hh = '0' + hh if len(hh) == 1 else hh
        return hh + ':' + mm + ':' + ss

    # [1] 계속 써먹을 변수 L1, L2와 total_time list 설정
    L1 = to_int(play_time) # 동영상 재생시간
    L2 = to_int(adv_time) # 광고 재생시간
    total_time = [0] * (L1 + 1) # 동영상 재생시간을 [0]의 list로 나타냄

    # [1-1] L1과 L2가 같다면 광고는 처음에 들어갈 수 밖에 없다.
    if L1 == L2:
        start_time = 0

    else:
        # [2] 시청자들의 재생 정보를 total_time에 담는다.
        # 여기서 total_time에는 시청자 수의 증감을 의미하게 된다.
        for log in logs:
            start, end = log.split('-')
            total_time[to_int(start)] += 1
            total_time[to_int(end)] -= 1

        # [3] total_time을 가공한다.
        # 여기서 total_time은 0초부터 i초까지의 누적 시청시간 합계를 의미하게 된다.
        watching = 0
        for i in range(1, L1 + 1):
            watching += total_time[i]
            total_time[i] = total_time[i - 1] + watching

        # [4] 가장 빠른 시작시간 start_time을 구한다.
        # 여기서 total_time[i] - total_time[i-L2]이 시청자들의 구간 누적 재생시간을 나타낸다.
        start_time = 0
        result = 0
        for i in range(L2-1, L1+1):
            if i == L2-1: # 시작 시간이 0인 경우 == total_time[i-L2]가 total_time[-1]이 되어버리므로
                if result < total_time[i]:
                    result = total_time[i]
                    start_time = i-L2+1
            else:
                if result < total_time[i] - total_time[i-L2]:
                    result = total_time[i] - total_time[i-L2]
                    start_time = i-L2+1

    answer = to_time(start_time)
    return answer