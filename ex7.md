# Exercise 7

## Question 1
The given reverse() function has a time complexity of O(n²) because it repeatedly scans the list to find elements, making it slower as the list grows. Each call to get_element_at_position(i) takes O(n) time, and since this is done for n elements, the total time becomes O(n²).

## Question 2
A better way to reverse the list is to go through it once and change the links directly, making it O(n). Instead of looking up each element repeatedly, we update the next pointers in a single pass. This makes the function much faster, especially for large lists.
