import collections
from itertools import combinations

# 다리위를 지나는 트럭
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

# 주식가격
# def stock_price(price):
#     answer = []
#     a = price[:]
#     count = 0   
#     for i in price:
#         for ix,j in enumerate(a):
#             if ix == 0:
#                 continue
#             if i <= j:
#                 count = count + 1 
#         a.pop(0)
#         answer.append(count)
#         count = 0
#     print(price)
#     return answer

#두 개 뽑아서 더하기
def two_number(number):
    answer = []
    #하나하나 더해보기
    # for i in range(len(number)):
    #     for j in range(i+1,len(number)):
    #         answer.append(number[i] + number[j])
    # answer = sorted(list(set(answer)))

    #조합을 이용해 문제 풀이
    a = list(combinations(number,2))
    for i in a:
        answer.append(i[0] + i[1])
    answer = list(set(answer))
    print(sorted(answer))
    return answer.sort()

if __name__ == "__main__":
    #####################################################################################################
    # 프로그래머스 다리위를 지나는 트럭
    # bridge_truck(2,10,[7,4,5,6])
    # bridge_truck(100,100,[10,10,10,10,10,10,10,10,10,10])
    # bridge_truck(100,100,[10])

    # 주식 가격
    # print(stock_price([1, 2, 3, 2, 3]))

    #두 개 뽑아서 더하기
    two_number([2,1,3,4,1])



