import collections
def solution(bridge_length, weight, truck_weights):
    answer = 1
    t = collections.deque()
    truck_weights.reverse()
    deq = collections.deque()

    while True:
        if t:
            t = collections.deque(map(lambda x: x+1,t))
            answer += 1
        if truck_weights and sum(deq) + truck_weights[-1] <= weight:
            deq.append(truck_weights.pop())
            t.append(0)
        if t[0] == bridge_length:
            t.popleft()
            deq.popleft()
        if not deq and not truck_weights:
            return answer

if __name__ == "__main__":
    #####################################################################################################
    # 프로그래머스 다리위를 지나는 트럭
    solution(2,10,[7,4,5,6])
    solution(100,100,[10,10,10,10,10,10,10,10,10,10])
    solution(100,100,[10])
