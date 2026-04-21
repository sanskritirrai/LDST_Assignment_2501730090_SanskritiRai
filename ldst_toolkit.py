# Dynamic Array

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize()

        self.arr[self.size] = x
        self.size += 1

    def _resize(self):
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        new_arr = [None] * (self.capacity * 2)

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity *= 2

    def pop(self):
        if self.size == 0:
            return "Array is empty"

        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def display(self):
        print([self.arr[i] for i in range(self.size)],
              f"(size={self.size}, capacity={self.capacity})")


# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_at_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete_by_value(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next
        else:
            print("Value not found")

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Doubly Linked List

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = DNode(x)
        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def insert_after(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new = DNode(x)
                new.next = temp.next
                new.prev = temp

                if temp.next:
                    temp.next.prev = new

                temp.next = new
                return
            temp = temp.next

        print("Target not found")

    def delete_at_position(self, pos):
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Stack using Singly Linked List

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return "Stack Underflow"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return "Empty Stack"
        return self.head.data


# Queue using Singly Linked List

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new = Node(x)
        if not self.tail:
            self.head = self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if not self.head:
            return "Queue Underflow"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return "Empty Queue"
        return self.head.data


# Task 4: Parentheses Checker

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.head is None:
                return False
            if stack.pop() != pairs[ch]:
                return False

    return stack.head is None


# MAIN (Test Cases)

if __name__ == "__main__":

    print("\n--- Dynamic Array ---")
    da = DynamicArray(2)
    for i in range(10):
        da.append(i)
        da.display()

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    da.display()

    print("\n--- Singly Linked List ---")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_end(5)
    sll.insert_at_end(7)
    sll.traverse()
    sll.delete_by_value(5)
    sll.traverse()

    print("\n--- Doubly Linked List ---")
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.insert_after(2, 99)
    dll.traverse()
    dll.delete_at_position(1)
    dll.traverse()

    print("\n--- Stack ---")
    st = Stack()
    st.push(10)
    st.push(20)
    print("Peek:", st.peek())
    print("Pop:", st.pop())

    print("\n--- Queue ---")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Front:", q.front())
    print("Dequeue:", q.dequeue())

    print("\n--- Parentheses Checker ---")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", is_balanced(t))