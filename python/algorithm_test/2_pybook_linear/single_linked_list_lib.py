#다음부터 만들때 head가 맨 앞 숫자를 가르키자(dummy가 사라지고 숫자가 채워지는 형식)
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
        if type(data) == type(SLinkedList()):
            # data.sll_next()
            self.tail.next = data.current
            data.sll_last()
            self.tail = data.current
            data.sll_first()
            self.num_of_data += (data.num_of_data-1)
            return
            
        new_node = sll_node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1
    #sll_leftappend 메소드 (맨 앞에 노드 추가)
    def sll_leftappend(self,data):
    #요소가 있고 없고를 나눈 이유 : 요소가 아무 것도 없을 때는 처음 넣은게 tail이 되어야 한다.
        new_node = sll_node(data)
        #요소가 아무것도 없을때 
        if self.num_of_data == 1:
            self.tail.next = new_node
            self.tail = new_node

            self.num_of_data += 1
            return
        #요소가 한개라도 있을 때
        new_node.next = self.head.next
        self.head.next = new_node

        self.num_of_data += 1

    #sll_delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
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
    
    #sll_pop 메소드 (맨 오른쪽에 있는 요소 제거)
    def sll_pop(self):
        if self.num_of_data == 1:
            print("error : empty!!")
            return None
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



    #sll_first 메소드(맨앞 요소로 가게 만듬 currnet가 맨앞으로 이동)
    def sll_first(self):
        if self.num_of_data == 1:
            return 1
        self.before = self.head
        self.current = self.head.next

        return self.current.data
    
    def sll_last(self):
        for _ in range(self.num_of_data):
            self.sll_next()
        
        return self.current.data
    #sll_next 메소드(다음 요소로 이동)
    def sll_next(self):
        if self.current.next == None:
            return None
        
        self.before = self.current
        self.current = self.current.next

        return self.current.data
    #sll_size 메소드 (linked list의 크기)
    def sll_size(self):
        return self.num_of_data
    #sll_print 메소드 (linked list안의 요소들을 모두 출력)
    def sll_print(self):
        self.sll_first()
        print("head -> ", end='')
        for _ in range(self.num_of_data-2):
            print(self.current.data, end = ' -> ')
            self.sll_next()
        print(self.current.data)
    
    def deepcopy(self):
        pop_deepcopy = SLinkedList()
        while self.current.next:
            pop_deepcopy.sll_append(self.sll_next())
        self.sll_first()
        return pop_deepcopy
