import matplotlib.pyplot as plt
import timeit
import sys

"""
1. Identify and explain the strategy used to grow arrays when full, with references to specific lines of code
in the file above. What is the growth factor?

First of all, the array size will not grow unless it is needed. That is, if the array still has space left, it
will not be expanded. The line that shows this is the following: 

if (allocated >= newsize && newsize >= (allocated >> 1)) {
        assert(self->ob_item != NULL || newsize == 0);
        Py_SET_SIZE(self, newsize);
        return 0;
    }

The most important part of this snippet is the conditional statement. Its condition means that, if the allocated
memory, i.e. capacity, is enough to hold the new size of the array, then we can just stop the function there, 
and there is no need to expand the array capacity.

If the condition evaluates as false, this means that size has reached capacity, and that the latter must be expanded.
Then, by how much will capacity grow? The answer is given in the line afterward (skipping the comments):

new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3; 

The size_t type has a size of at least 16 bits and is unsigned. This is important because the expression performs bit-wise operations
NOT (~) and AND (&) to determine new_allocated. 3 in 16-bit unsigned binary is (12 zeros)_0011, which results in (12 ones)_1100.
The above result is a multiple of 4. This result and the AND operation ensures that new_allocated is a multiple of four. 

Now let's look at the other side of the expression. newsize + (newsize >> 3) + 6. >> is a bit shift operator, which will shift every bit
in newsize three times to the right; effectively performing integer division by 8. 

The result is ANDed with the aforementioned ~3. What essentially happens here is that every time new_allocated is increased by one eight
of its previous value. However because of the added 6, which is needed to start the sequence, it is not always an exact increase of 12.5%, 
at least initially. This leads to the provided sequence in the code of 0, 4, 8, 16, 24, 32, 40, 52, 64, 76, ...

In short, the growth factor is around 1.125 (i.e a 12.5% increase each time).

"""

array = []
expected_size = sys.getsizeof(array)

for i in range(64):
    array.append(i)
    current_size = sys.getsizeof(array)
    if current_size != expected_size:
        print("Capacity increased on element", i)
        expected_size = current_size

print("\n")
# From running the above code excerpt we were able to determine that S = 52.

array1times = []
for i in range(1000):
    array1 = []
    for j in range(52):
        array1.append(j)
    array1times.append(timeit.timeit(stmt= lambda: array1.append(52), number= 1))

print(f"Average time for Appending to array of 52 elements: {sum(array1times)/len(array1times)}")

array2times = []
for i in range(1000):
    array2 = []
    for j in range(51):
        array2.append(j)
    array2times.append(timeit.timeit(stmt= lambda: array2.append(51), number= 1))

print(f"Average time for Appending to array of 51 elements: {sum(array2times)/len(array2times)}")

plt.figure()
plt.title("Append times starting at 52 elements")
plt.xlabel("Time (s)")
plt.hist(x=array1times, color= "red")
plt.savefig("ex3.5.1.png")
plt.show()

plt.figure()
plt.title("Append times starting at 51 elements")
plt.xlabel("Time (s)")
plt.hist(x=array2times, color= "blue")
plt.savefig("ex3.5.2.png")
plt.show()

"""
5. Do you see any difference? Why?

There is a distinguishable difference on average due to the increased time it takes to reallocate the dynamic array,
although the variance in time elapsed is in fact very small. The reason it is not that significant is likely due to
the sizes being examined here. If we were resizing arrays of thousands of elements, reallocation would take much 
longer and therefore would be more of a nuisance. However, due to how fast computers are nowadays, this effect 
will be minimal on arrays of smaller sizes, such as the ones discussed here.

"""