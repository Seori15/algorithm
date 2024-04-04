from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    def move():
        # 1초 진행
        bridge.append(0)
        return bridge.popleft()

    time = 0
    now_weight = 0
    bridge, truck_weights = deque(0 for _ in range(bridge_length)), deque(truck_weights)
    while truck_weights:
        # [1] 1초 진행
        now_weight -= move()
        time += 1
        next = truck_weights[0]
        # [2] 다리가 무게를 못견디면 트럭이 다리를 지날 때까지 기다린다.
        while now_weight + next > weight:
            # 트럭이 다리를 빠져나올 때까지 1초씩 진행
            while bridge[0] == 0:
                move()
                time += 1
            now_weight -= move()
            time += 1
        # [3] 다음 트럭이 다리에 올라온다.
        truck_weights.popleft()
        bridge[-1] = next
        now_weight += next

    return time + bridge_length