#stack.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 테스트
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()  # Output: 30 -> 20 -> 10 -> None

print(stack.pop())  # Output: 30
print(stack.peek()) # Output: 20
print(stack.pop())  # Output: 20
print(stack.pop())  # Output: 10

# 스택이 비었을 때 pop이나 peek를 호출하면 예외 발생
# print(stack.pop())  # Raises IndexError
# print(stack.peek()) # Raises IndexError