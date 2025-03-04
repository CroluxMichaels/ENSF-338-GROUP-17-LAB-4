# Exercise 5 - Reflecting on measurements

## Question 1
The two approaches handle measurement noise differently. 

- `timeit.timeit()` runs the given function multiple times (specified by `number`) and returns the total execution time. 
   This approach is useful for reducing the impact of fluctuations in execution time by averaging over multiple iterations.
- `timeit.repeat()`, on the other hand, runs the timing experiment multiple times (specified by `repeat`), each time performing 
   the function execution `number` times. This then helps to capture variations of multiple test runs, which is useful when 
   assessing the consistency and stability of execution time.

When to use:
- `timeit.timeit()` when we want a single, averaged execution time to reduce short-term noise
- `timeit.repeat()` when we want multiple timing results to understand variations across runs and maybe detect inconsistencies


## Question 2

- **For `timeit.timeit()`**: The **average** is useful since the function is executed multiple times in a single run, reducing "noise".
- **For `timeit.repeat()`**: The **minimum** execution time is the best metric, as it likely represents the case with "minimal" system 
                             interference like for example, there is no background process interruptions. Moreover, the **max** execution 
                             time can help identify outliers, but it is generally less useful due to some external factors.

Thus, `min(timeit.repeat(...))` is a commonly used measurement to get the most reliable estimate of execution time.

