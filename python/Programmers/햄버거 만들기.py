# 각 재료를 사용하여 햄버거를 만드는 모든 경우의 수 조합 중, 조건에 맞는 방법의 수 찾기
def solution(ingredient, k, s):
    answer = 0
    n = len(ingredient)

    # [1] 1<<n 은 길이가 n인 리스트에서 모든 조합 경우의 수를 고려하게 해준다.
    for num in range(1, 1<<n):
        k_sum = 0
        s_sum = 0
        # [2] 현재 반복문에서 선택된 재료들의 합을 구한다.
        for idx in range(0, n):
            if (num & (1 << idx)) != 0:
                k_sum += ingredient[idx][0]
                s_sum += ingredient[idx][1]
        if k_sum <= k and s_sum >= s:
            answer += 1 
    return answer