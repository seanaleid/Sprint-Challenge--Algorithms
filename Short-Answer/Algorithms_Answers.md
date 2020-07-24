#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Thr urn time is O(n^c) - Polynomial because it takes more steps the larger n gets. We have to multiply n*n until we meet the condition.


b) The run time is O(n log n) - Linearithmic because j is less than n. J cannot be applied to every i if i starts at 1. The inner loop does not initialize until i is greater than 1. 


c) This run time is O(n) - Linear because no matter the size of the bunnies, each time the function is called, it will increase by two bunnies. 

## Exercise II

The solution to this exercise is a divide and conquer strategy. Assuming the list of floors is in a sorted list:

    Start at the mid point and run a check. 
        If the egg breaks, we can assume that the mid point and all elements to the right are the same. Find the mid point of the sub list from the first element to the current mid point. Run another check.

        Else, we need to move to the mid point of the sub list starting at the current mid point to the end and check again. 

    We follow this logic until we find the mid point that matches our target. 

This strategy is O(log n) because we are halving each time until we find our target. O(log n) of 10 elements is ~3steps, of 100 is ~6steps, 1000 is ~9steps, etc. in the worst case. 

