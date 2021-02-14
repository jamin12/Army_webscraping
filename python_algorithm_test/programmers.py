from collections import deque

# 다리위를 지나는 트럭
def bridge_truck(bridge_length, weight, truck_weights):
    answer = 0
    t = deque()
    truck_pass = deque()
    truck_weights.reverse()
    s = 0
    while True:
        if not truck_pass and not truck_weights:
            break
        answer += 1
        if t:
            t = deque(map(lambda x: x+1,t))
            if t[0] >= bridge_length:
                t.popleft()
                i = truck_pass.popleft()
                s -= i
        if truck_weights:
            if s + truck_weights[-1] <= weight:
                i = truck_weights.pop()
                t.append(0)
                truck_pass.append(i)
                s += i
                
    return answer

    

if __name__ == "__main__":
    #####################################################################################################
    # 프로그래머스 다리위를 지나는 트럭
    bridge_truck(2,10,[7,4,5,6])
    bridge_truck(100,100,[10])
    bridge_truck(100,100,[10,10,10,10,10,10,10,10,10,10])




