# ex4.1.py

# Q1: Complexity Analysis
# Best case: O(n), Worst case: O(n²), Average case: O(n²)

def processdata(li):
    for i in range(len(li)):  
        if li[i] > 5:
            for j in range(len(li)):  
                li[i] *= 2

# Q2: Modified version with same best, worst, and average case complexity (O(n²))
def processdata_modified(li):
    for i in range(len(li)):  
        for j in range(len(li)):  
            li[i] *= 2

