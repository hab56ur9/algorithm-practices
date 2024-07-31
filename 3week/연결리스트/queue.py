class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        temp = self.front
        self.front = temp.next
        
        if self.front is None:
            self.rear = None
        
        return temp.data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def print_queue(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 테스트
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.print_queue()  # Output: 10 -> 20 -> 30 -> None

print(queue.dequeue())  # Output: 10
print(queue.peek())     # Output: 20
print(queue.dequeue())  # Output: 20
print(queue.dequeue())  # Output: 30

# 큐가 비었을 때 dequeue나 peek를 호출하면 예외 발생
# print(queue.dequeue())  # Raises IndexError
# print(queue.peek())     # Raises IndexError