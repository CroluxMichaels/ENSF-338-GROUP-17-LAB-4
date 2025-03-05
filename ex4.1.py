# ex4.1.py

# Q1: Complexity Analysis
# Best case: O(n), no element in li is greater than 5 and the inner loop never executes
# Worst case: O(n²), if all elements are greater than 5, the inner loop runs for every iteration of the outer loop
# Average case: O(n²), this is because it depends on the number of the elements greater than 5. If half of the 
# elements trigger the inner loop then the complexity is around O(n²) in the asymptotic sense.

def processdata(li):
    for i in range(len(li)):  
        if li[i] > 5:
            for j in range(len(li)):  
                li[i] *= 2

# Q2: Modified version with same best, worst, and average case complexity O(n²)
# just removed the conditional inner loop to ensure the inner loop always runs
def processdata_modified(li):
    for i in range(len(li)):  
        for j in range(len(li)):  
            li[i] *= 2

