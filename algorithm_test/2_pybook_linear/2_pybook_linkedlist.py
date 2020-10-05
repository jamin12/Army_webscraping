import collections
import re
import sys
from single_linked_list_lib import *

def isPalindrome(head : SLinkedList):
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
    # q = collections.deque()

    # for i in head:
    #     q.append(i)
    
    # while len(q) > 1:
    #     if q.popleft() != q.pop():
    #         return False
    # return True
#런너를 이용
    """
    한개는 두칸씩 한개는 한칸씩 움직이면 한칸씩 움직인게
    두칸씩 움직인것이 끝에 도달 했을때 한칸씩 움직인것은 정확이 반만큼 간다
    한칸씩 이동 할때 다른 변수에다 역순으로 저장 한 후 
    한칸씩 이동한 것과 역순으로 저장한 것을 비교
    ex) 1->2->3->2->1 
    역순에는 2->1 이 저장 한칸씩 이동한것은 2->1이 남아있음(이동 할수있는 거리가) 이제 비교하면서 한칸씩 이동
    """
    rev = SLinkedList()
    fast = head
    slow = head.deepcopy()

    slow.sll_next()
    while fast and fast.current.next:
        fast.sll_next()
        fast.sll_next()
        rev.sll_leftappend(slow.current.data)
        slow.sll_next()
    if fast.num_of_data % 2 == 0:
        slow.sll_next()
    rev.sll_next()

    while rev.current.next and rev.current.data == slow.current.data:
        slow.sll_next()
        rev.sll_next()
    
    if slow.current.data != rev.current.data:
        return False
    return not rev.current.next

def margeTwoLists(l1,l2):
    pass
    

#파이썬은 linked list가 일반 list에 구현이 다 되어있다.(이런 개꿀이?? ㅋㅋㅋㅋㅋ)
if __name__ == "__main__":
##########################################################################
    #팰린드롬 연결 리스트 : 연결 리스트가 팰린드롬 구조인지 판별하라
    #linked list라는 자료구조형이 파이썬에 따로 없어서 iter를 사용함 iter : 데이터를 하나하나 처리할수 있는 자료형
    # i = SLinkedList()
    # i.sll_append(1)
    # i.sll_append(2)
    # i.sll_append(3)
    # i.sll_append(2)
    # i.sll_append(1)
    # i.sll_append(1)
    # i.sll_append(1)
    # i.sll_append(2)
    # i.sll_append(3)
    # i.sll_append(2)
    # i.sll_append(1)
    # sPalindrome(i)
##########################################################################
    #두 정렬 리스트의 병합 : 정렬되어 있는 두 연결 리스트를 합쳐라
    l1 = SLinkedList()
    l1.sll_append(1)
    l1.sll_append(2)
    l1.sll_append(4)
    l2 = SLinkedList()
    l2.sll_append(1)
    l2.sll_append(3)
    l2.sll_append(4)
    margeTwoLists(l1,l2)