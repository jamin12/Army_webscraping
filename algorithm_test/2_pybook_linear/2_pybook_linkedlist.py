import collections
import re
import sys


def isPalindrome(head):
#책 풀이 : 연결 리스트가 처음이라서 내 풀이는 없다.
#이 방법은 역시 별로... pop(0)이 시간 복잡도 O(n)이라서 총 O(n^2)이 되버림
    # q = []

    # if not head:
    #     return True
    
    # node = head
    # while node is not None:
    #     q.append(node.val)
    #     node = node.next
    
    # while len(q) > 1:
    #     if q.pop(0) != q.pop():
    #         return False

    # return True
#데큐를 이용
    q = collections.deque()

    for i in head:
        q.append(i)
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True


#파이썬은 linked list가 일반 list에 구현이 다 되어있다.(이런 개꿀이?? ㅋㅋㅋㅋㅋ)
if __name__ == "__main__":
##########################################################################
    #팰린드롬 연결 리스트 : 연결 리스트가 팰린드롬 구조인지 판별하라
    #linked list라는 자료구조형이 파이썬에 따로 없어서 iter를 사용함 iter : 데이터를 하나하나 처리할수 있는 자료형
    isPalindrome(iter([1,2,2,1]))