import collections
import re
import sys

def twoSum(nums, target):
    #브루트 포스로 계산(모든 인수를 하나하나 더해서 답을 구함) 시간복잡도 높음 효율성이 매우 떨어짐
    # for i in range(len(nums)):
    #     for j in range(i + 1,len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]
    #in을 이용한 탐색
        #내 풀이
    # for i in nums:
    #     if abs(i - target) in nums:
    #         return [nums.index(i),nums.index(abs(i-target))]
        #책 풀이
    # for i,n in enumerate(nums):
    #     complement = target - n
    #     if complement in nums[i+1:]:
    #         return nums.index(n) , nums[i+1:].index(complement) + (i+1) # i+1를 하는 이유 : nums[i+1:]을 하기 때문에 인덱스 값이 i만큼 줄어들어서 더해 주게 된다
    # 첫 번째 수를 뺀 결과 키 조회(딕셔너리에 넣음으로써 탐색이나 비교 없이 한번에 찾아내는게 가능)
    nummap = {}
    for i, n in enumerate(nums):
        nummap[n] = i

    for i , n in enumerate(nums):
        if target - n in nummap and i != nummap[target-n]:
            return nums.index(n), nummap[target-n]

def trap(height):
    #투 포인터를 최대로 이동
    # if not height:
    #     return 0
    
    # volume = 0
    # left,right = 0 ,len(height)-1
    # left_max , right_max = height[left], height[right]

    # while left<right:
    #     left_max, right_max = max(height[left],left_max), max(height[right],right_max)
        
    #     if left_max <= right_max:
    #         volume += left_max - height[left]
    #         left += 1
    #     else :
    #         volume += right_max - height[right]
    #         right -= 1
    # return volume

    #스택을 이용해 풀이
    stack = []
    volume = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break
            

            distance = i - stack[-1] -1
            waters = min(height[i],height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume

def threesum(nums):
    #내 풀이
    # result = []
    # nums.sort()

    # for i in range(len(nums) - 1):
    #     left , right = i + 1, len(nums) - 1
    #     if i > 0 and nums[i] == nums[-1]:
    #         continue
    #     while left<right :
    #         if [nums[i],nums[left],nums[right]] in result:
    #             break
    #         if nums[i] + nums[left] + nums[right] == 0:
    #             result.append([nums[i],nums[left],nums[right]]) 
    #         # nums를 정렬 했기 때문에 더한게 0보다 크면 오른쪽을 옮김
    #         if nums[i] + nums[left] + nums[right] > 0:
    #             right -= 1
    #         else :
    #             left += 1
    # return result
    # 책 풀이
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left ,right = i + 1 ,len(nums) - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums < 0:
                left += 1
            elif sums > 0:
                right -= 1
            else:
                results.append((nums[i],nums[left],nums[right]))
                
                #같은 값이 있으면 무의미 하기 때문에 스킵
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                #어차피 합이 0 이고 한쪽만 움직여봤자 당연하게 0이 아니게 된다 그러므로 둘다 움직임
                left += 1 
                right -= 1

    return results



def arrayPairSum(nums):
    # # 내 풀이
    # nums.sort()
    # def divive_list(l,n):
    #     for i in range(0,len(l),n):
    #         yield l[i:i+n] # yield 를 이용해 리스트를 2 씩 나눴다 yield : 반환 값이 하나가 아닌 여러게로 할 수 있게 해줌
    # divied = list(divive_list(nums,2))
    # # print(divied)
    # result = []
    # for x,y in divied:
    #     result.append(min(x,y))

    # return sum(result)
    # 책 풀이 : 오름차순 풀이
    # sum = 0
    # pair = []
    # nums.sort()

    # for n in nums:
    #     pair.append(n)
    #     #페어의 길이가 2가되면(즉 두개씩 나누게 되는 것임) 최솟값을 구하고 다시 비워준다
    #     if len(pair) == 2:
    #         sum += min(pair)
    #         pair = []
    
    #짝수 번째 값 계산 : 어차피 짝수 번째 숫자가 더해 질거니 이렇게 함
    # sums = 0
    # nums.sort()

    # for i, n in enumerate(nums):
    #     if i % 2 == 0:
    #         sums += n

    # return sums
    #파이썬 다운 방식 : 이건 진짜 생각도 못함
    return sum(sorted(nums)[::2])

def productExceptSelf(nums):
    # 내 풀이 : 하지만 나눗셈을 하지 말라는걸 나중에 봄....
    # def mutiply(li):
    #     muti = 1
    #     for i in li:
    #         if i == 0:
    #             return 0
    #         muti *= i
    #     return muti
    # return [mutiply(nums) / i for i in nums]
    #책 풀이
    #정확한 이유는 모르겠지만 왼쪽으로 곱한거랑 오른쪽으로 곱한거랑 곱하면 된대.... 이게 수학적 공식이 있긴한가.??
    #아무튼 이해는 했는데.... 좀 그렇다
    out = []
    p = 1
    for i in range(0,len(nums)):
        out.append(p)
        p = p * nums[i]
    
    p = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p*nums[i]
    return out

def maxProfit(prices):
    #내 풀이
    #책 풀이도 이거랑 똑같은데 시간 복잡도가 너무 높아서 실패
    # maxv = 0
    # for i in range(len(prices)):
    #     for j in range(i+1,len(prices)):
    #         if (prices[j] - prices[i]) > maxv:
    #             maxv = prices[j] - prices[i]
    # return maxv
    #책 풀이
    profit = 0
    vmax = sys.maxsize
    for i in prices:
        vmax = min(vmax,i)
        profit = max(profit,i-vmax)
    return profit
        
        


if __name__ == '__main__':
##########################################################################
    #두 수의 합 // 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
    # twoSum([2,7,11,15],9)
##########################################################################
    #빗물 트래핑 // 높이를 입력받아 비온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라
    #이건 진짜 이해를 못하겠네 수발 ㅡㅡ
    # trap([0,1,0,2,1,0,1,3,2,1,2,1])
##########################################################################
    #세 수의 합 //배열을 입력 받아 합으로 0을 만들 수 있는 3개의 엘리 먼트를 출력해라
    # threesum([-1,0,1,2,-1,-4])
##########################################################################
    #n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
    # print(arrayPairSum([1,4,3,2]))
##########################################################################
    # 자신을 제외한 배열의 곱 : 배열은 입력받아 output[i]가 자신을 제외한 나머지 요소의 곱셈 결과가 되도록 출력하라
    # print(productExceptSelf([1,2,3,4]))
##########################################################################
    #주식을 사고팔기 가장 좋은 시점 : 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
    maxProfit([7,1,5,3,6,4])


