import collections
import re
import sys

#linked list
class sll_node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    #초기화 메소드
    def __init__(self):
        dummy = sll_node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = self.head
        self.before = None

        self.num_of_data = 1
    #append 메소드(insert - 맹 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def sll_append(self, data):
        #tail에 더했는데 head도 추가 되는 이유 : 둘다 dummy로 초기화 했기 때문에 주소 값이 같다 
        #결과적으로 tail에 추가 한게 head에도 추가 된다.
        new_node = sll_node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1
    #leftappend 메소드 (맨 앞에 노드 추가)
    def sll_leftappend(self,data):
    #요소가 있고 없고를 나눈 이유 : 요소가 아무 것도 없을 때는 처음 넣은게 tail이 되어야 한다.
        new_node = sll_node(data)
        #요소가 아무것도 없을때 
        if self.num_of_data == 0:
            self.tail.next = new_node
            self.tail = new_node

            self.num_of_data += 1
            return
        #요소가 한개라도 있을 때
        new_node.next = self.head.next
        self.head.next = new_node

        self.num_of_data += 1
    #delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def sll_delete(self):
        pop_data = self.current.data
        
        # == 이아닌 is를 쓴 이유 : ==은 값을 비교해 false ,true를 가려낸다, is는 객체를 비교해서 false ,true를 가려내기 때문에 is가 더 적절하다
        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before # 중요 : current 가 next가 아닌 before로 변경된다.

        self.num_of_data -= 1

        return pop_data

    #sll_leftpop 메소드 (맨 왼쪽에 있는 요소를 제거)
    def sll_leftpop(self):
        pop_data = self.head.next
        self.head.next = pop_data.next

        # TODO: 가비지 콜렉션 좀더 공부
        #가비지 컬랙션이 알아서 없애 주므로 할필요 없음 (가비지 컬랙션 : 참조 횟수가 0이 된 객체를 메모리에서 해체)
        # pop_data.data = None
        # pop_data.next = None

        self.num_of_data -= 1
        return pop_data

    #TODO:정렬 기능 만들어 보기

    #sll_pop 메소드 (맨 오른쪽에 있는 요소 제거)
    def sll_pop(self):
        pop_data = self.head
        if self.current is self.tail:
            self.tail = self.before
            self.tail.next = None
            self.current = self.tail

        for _ in range(self.num_of_data-1):
            pop_data = pop_data.next

        pop_data_really = pop_data.next.data
        pop_data.next = None

        self.num_of_data -= 1
        return pop_data_really



    #first 메소드(맨앞 요소로 가게 만듬 currnet가 맨앞으로 이동)
    def sll_first(self):
        if self.num_of_data == 0:
            return 0
        self.before = self.head
        self.current = self.head.next

        return self.current.data
    #s_next 메소드(다음 요소로 이동)
    def sll_next(self):
        if self.current.next == None:
            return None
        
        self.before = self.current
        self.current = self.current.next

        return self.current.data
    #SLLsize 메소드 (linked list의 크기)
    def sll_size(self):
        return self.num_of_data
    #SLLprint 메소드 (linked list안의 요소들을 모두 출력)
    def sll_print(self):
        node = self.head.next
        print("head -> ", end='')
        for _ in range(self.num_of_data-1):
            print(node.data, end = ' -> ')
            node = node.next
        print(node.data)

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
    rev = None
    # slow = fast = head
    # while fast and fast.next:
    #     fast = fast.sll_next().next
    #     rev, rev.sll_next,slow = slow, rev, slow.sll_next
    # if fast:
    #     slow = slow.sll_next
    
    # while rev and rev.current.data == slow.current.data:
    #     slow, rev = slow.sll_next, rev.sll_next
    
    return not rev

    

#파이썬은 linked list가 일반 list에 구현이 다 되어있다.(이런 개꿀이?? ㅋㅋㅋㅋㅋ)
if __name__ == "__main__":
##########################################################################
    #팰린드롬 연결 리스트 : 연결 리스트가 팰린드롬 구조인지 판별하라
    #linked list라는 자료구조형이 파이썬에 따로 없어서 iter를 사용함 iter : 데이터를 하나하나 처리할수 있는 자료형
    # isPalindrome([ListNode(1),ListNode(2),ListNode(2),ListNode(1)])
    i = SLinkedList()
    i.sll_append(1)
    i.sll_append(2)
    i.sll_append(2)
    i.sll_append(1)
    print(i.current.data)
    for _ in range(i.num_of_data):
        print(i.current.data)
        i.sll_next()
    # isPalindrome(i)