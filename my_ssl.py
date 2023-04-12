# 학번: 202003613 / 학과: 글로벌스포츠산업학부 / 이름: 최진원
# 정상 동작
# Node 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList 클래스 정의
class LinkedList:
    # 초기화 메소드
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.before = None
        self.num_of_data = 0

    # append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data += 1

    # delete 메소드 (delete - current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        pop_data = self.current.data
        if self.current is self.tail:
            self.tail = self.before
            # 중요 : current가 next가 아닌 before로 변경된다.
            self.before.next = self.current.next
            self.current = self.before
            self.num_of_data -= 1
        return pop_data

    # first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
        if self.num_of_data == 0:
            return None
        self.before = self.head
        self.current = self.head.next
        return self.current.data

    # next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next == None:
            return None
        self.before = self.current
        self.current = self.current.next
        return self.current.data

    # size 메소드
    def size(self):
        return self.num_of_data

    # traverse_all 메소드 (head부터 tail까지 각 노드를 순차적으로 탐색하며 각 노드의 data를 출력함)
    def traverse_all(self):
        node = self.head.next
        result = "head"
        while node != None:
            result += " -> " + "(" + str(node.data) + ")"
            node = node.next
        result += " -> null"
        print(result)

    # insert_at 메소드 (리스트의 주어진 위치에 new_data를 삽입함)
    def insert_at(self, position, new_data):
        if position <= 0:
            print("error")
            return
        elif position > self.num_of_data:
            self.append(new_data)
        else:
            new_node = Node(new_data)
            node = self.head
            for i in range(position - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
            self.num_of_data += 1

    # remove 메소드 (리스트의 원소 가운데 key값과 일치하는 원소를 모두 삭제하고, 리스트를 수정함)
    def remove(self, key):
        node = self.head.next
        before_node = self.head
        index = 1
        removed_indexes = []
        while node != None:
            if node.data == key:
                before_node.next = node.next
                if node is self.tail:
                    self.tail = before_node
                print(f"{index}번째 원소를 삭제합니다.")
                removed_indexes.append(index)
            else:
                before_node = node
            node = node.next
            index += 1
        if not removed_indexes:
            print("해당하는 원소가 없습니다.")

# 추가 함수에 대한 예문
linked_list = LinkedList()

linked_list.append(100)
linked_list.append(72)
linked_list.append(325)
linked_list.traverse_all()
print()

linked_list.insert_at(0, 150)
linked_list.insert_at(2, 150)
linked_list.traverse_all()
linked_list.insert_at(10, 150)
linked_list.traverse_all()
print()

linked_list.remove(75)
linked_list.traverse_all()
linked_list.remove(150)
linked_list.traverse_all()