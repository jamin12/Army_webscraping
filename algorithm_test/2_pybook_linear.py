import collections
import re

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
    if not height:
        return 0
    
    volume = 0
    left,right = 0 ,len(height)-1
    left_max , right_max = height[left], height[right]

    while left<right:
        left_max, right_max = max(height[left],left_max), max(height[right],right_max)
        
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else :
            volume += right_max - height[right]
            right -= 1
    return volume


if __name__ == '__main__':
##########################################################################
    #두 수의 합 // 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
    # twoSum([2,7,11,15],9)
##########################################################################
    #빗물 트래핑 // 높이를 입력받아 비온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라
    trap([0,1,0,2,1,0,1,3,2,1,2,1])
