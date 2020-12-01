import collections
# def bridge_truck(bridge_length, weight, truck_weights):
#     answer = 1
#     t = collections.deque()
#     truck_weights.reverse()
#     deq = collections.deque()

#     while True:
#         if t:
#             t = collections.deque(map(lambda x: x+1,t))
#             answer += 1
#         if truck_weights and sum(deq) + truck_weights[-1] <= weight:
#             deq.append(truck_weights.pop())
#             t.append(0)
#         if t[0] == bridge_length:
#             t.popleft()
#             deq.popleft()
#         if not deq and not truck_weights:
#             return answer

def stock_price(price):
    

    return 0


if __name__ == "__main__":
    #####################################################################################################
    # 프로그래머스 다리위를 지나는 트럭
    # bridge_truck(2,10,[7,4,5,6])
    # bridge_truck(100,100,[10,10,10,10,10,10,10,10,10,10])
    # bridge_truck(100,100,[10])

    # 주식 가격
    stock_price([1, 2, 3, 2, 3])


