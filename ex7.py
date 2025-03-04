import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_element_at_position(self, pos):
        current = self.head
        index = 0
        while current and index < pos:
            current = current.next
            index += 1
        return current if current else None

    def reverse_quadratic(self):  # O(n^2) reverse
        new_head = None
        prev_node = None
        for i in range(self.get_size() - 1, -1, -1):
            curr_node = self.get_element_at_position(i)
            curr_new_node = Node(curr_node.data)
            if new_head is None:
                new_head = curr_new_node
            else:
                prev_node.next = curr_new_node
            prev_node = curr_new_node
        self.head = new_head
    
    def reverse_optimized(self):  # O(n) reverse
        prev, current = None, self.head
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev

def measure_time(reverse_method, linked_list):
    start = time.time()
    reverse_method()
    end = time.time()
    return end - start

sizes = [1000, 2000, 3000, 4000]
n_iterations = 100
results_quadratic, results_optimized = [], []

for size in sizes:
    total_time_quadratic = 0
    total_time_optimized = 0
    
    for _ in range(n_iterations):
        linked_list = SinglyLinkedList()
        for i in range(size):
            linked_list.insert_tail(i)
        total_time_quadratic += measure_time(linked_list.reverse_quadratic, linked_list)
        
        linked_list = SinglyLinkedList()
        for i in range(size):
            linked_list.insert_tail(i)
        total_time_optimized += measure_time(linked_list.reverse_optimized, linked_list)
    
    results_quadratic.append(total_time_quadratic / n_iterations)
    results_optimized.append(total_time_optimized / n_iterations)

plt.figure(figsize=(8, 5))
plt.plot(sizes, results_quadratic, label='O(n^2) Given Reverse()', marker='o', linestyle='--', color='r')
plt.plot(sizes, results_optimized, label='O(n) Optimized Reverse()', marker='s', linestyle='-', color='b')
plt.xlabel("List Size")
plt.ylabel("Time (seconds)")
plt.title("Performance Comparison: Given vs Optimized Reverse()")
plt.legend()
plt.grid()
plt.show()