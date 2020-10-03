import collections
import re
import sys

#linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #초기화 메소드
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0
    #append 메소드(insert - 맹 뒤에 노드 추가, atail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1
    #delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before # 중요 : current 가 next가 아닌 before로 변경된다.

        self.num_of_data -= 1

        return pop_data
    def first(self):
        if self.num_of_data == 0:
            return 0
        self.before = self.head
        self.current = self.head.next
        
        return self.current.data

    def s_next(self):
        if self.current.next == None:
            return None
        
        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data

                
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
    # q = collections.deque()

    # for i in head:
    #     q.append(i)
    
    # while len(q) > 1:
    #     if q.popleft() != q.pop():
    #         return False
    # return True
    # rev = None
    # slow = fast = head
    # while fast and fast.next:
    #     rev, rev.next, slow = slow, rev, slow.next
    pass

#파이썬은 linked list가 일반 list에 구현이 다 되어있다.(이런 개꿀이?? ㅋㅋㅋㅋㅋ)
if __name__ == "__main__":
##########################################################################
    #팰린드롬 연결 리스트 : 연결 리스트가 팰린드롬 구조인지 판별하라
    #linked list라는 자료구조형이 파이썬에 따로 없어서 iter를 사용함 iter : 데이터를 하나하나 처리할수 있는 자료형
    # isPalindrome([ListNode(1),ListNode(2),ListNode(2),ListNode(1)])
    i = LinkedList()
    i.append(5)
    i.append(4)
    i.append(2)
    i.append(3)
    i.append(1)
    i.append(1)
    i.append(2)
    i.append(3)
    i.append(4)
    print(i.first())
    print(i.s_next())
    print(i.size())
    print(i.tail.data)
    print(i.current.data)
    