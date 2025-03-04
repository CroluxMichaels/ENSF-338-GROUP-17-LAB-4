import time
import matplotlib.pyplot as plt

# Q1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert data into the linked list in sorted order."""
        new_node = Node(data)
        if not self.head or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def display(self):
        """Display the linked list elements."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

#Q2
def binary_search_linked_list(linked_list, target):
    """Performs binary search on a sorted linked list."""
    start = linked_list.head
    end = None
    
    while start != end:
        mid = get_middle(start, end)
        
        if mid.data == target:
            return True  # Element found
        elif mid.data < target:
            start = mid.next  # Search in right half
        else:
            end = mid  # Search in left half
    
    return False  # Element not found

def get_middle(start, end):
    """Finds the middle node between start and end in a linked list."""
    slow = start
    fast = start
    while fast != end and fast.next != end:
        slow = slow.next
        fast = fast.next.next
    return slow


#Q3
class Array:
    def __init__(self):
        self.data = []

    def insert(self, num):
        """Insert in sorted order."""
        self.data.append(num)
        self.data.sort()

    def binary_search(self, target):
        """Binary search using a standard approach."""
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[mid] == target:
                return True
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

#Q4. You already know that complexity of binary search for array is O(logn). What is the complexity of binary search for linked lists?
# (explain in your own words, do not just copy/paste from the sites above)

# Finding the middle requires O(n), making each step O(n). Binary search does log n steps, this results to O(n log n) complexity. 
# This also shows that the binary search in linkedlist is inefficient compared to an array. 

#Q5
def measure_time(search_function, structure, values, target):
    """Measure execution time of a search function."""
    start_time = time.time()
    search_function(structure, target)
    return (time.time() - start_time) * 1000  # Convert to ms

sizes = [1000, 2000, 4000, 8000]
linked_list_times = []
array_times = []

for size in sizes:
    # Create structures
    linked_list = LinkedList()
    array = Array()
    values = list(range(size))
    
    for value in values:
        linked_list.insert(value)
        array.insert(value)
    
    target = size // 2  # Middle value

    # Measure search times
    linked_list_times.append(measure_time(binary_search_linked_list, linked_list, values, target))
    array_times.append(measure_time(lambda arr, num: arr.binary_search(num), array, values, target))

# Plot results
plt.plot(sizes, linked_list_times, label="Linked List Binary Search", marker="o")
plt.plot(sizes, array_times, label="Array Binary Search", marker="o")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")
plt.title("Binary Search Performance: Linked List vs Array")
plt.legend()
plt.show()
