# Exercise 6

## Question 1

Arrays allow fast access to elements (complexity of (O(1))) but take time (complexity of (O(n))) to insert or delete elements due to shifting. Linked lists allow easy insertions and deletions (complexity of (O(1))), but accessing elements is slower (complexity of (O(n))) because you have to traverse the list. Arrays use contiguous memory, making them better for fast & random access, while linked lists are more flexible for dynamic changes, such as inserting or deleting elements.

## Question 2

To reduce the impact of both deletion and insertion, both tasks must be performed together. Instead of deleting and inserting separately, overwrite the element and shift other elements just once. This reduces unnecessary operations and makes the process more efficient, especially for large arrays.

## Question 3

- Insertion Sort: It works well for linked lists because inserting an element in place is easy. But it’s still slow with O(n²) time complexity for large lists.
- Merge Sort: It is best for linked lists as it works in O(n log n) time and doesn’t require extra space for merging, unlike arrays.

## Question 4

Insertion sort has O(n²) complexity for both arrays and linked lists but is faster for linked lists. Merge sort has O(n log n) complexity for both, but it’s better for linked lists because it doesn’t need extra space for merging, as with arrays. Merge sort is the most efficient for large linked lists.