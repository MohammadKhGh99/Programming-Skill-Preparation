# 1 - Analyze the time complexity of the sorting algorithms you implemented earlier.

# Bubble sort - there are two loops one nested in another,
# both of them iterate in worst cast O(N) iteration (if the length of the array is N), other code lines are basic and
# their Time Complexity is O(1), so the total Time Complexity in worst case will be O(N^2)

# Merge Sort - in merge sort we have called the function recursively twice, in each one we were divide the array into 2
# equal-length arrays, so each function call will make O(log(N)) (if the length of the array is N)
# so this is 2*O(log(N)), and then we iterate over all the elements in the array to merge them in new one
# so this merging will take O(N), we notice that this iteration is inside each recursive call
# so the total Time Complexity will be O(Nlog(N))

# Quick Sort - the partition function will take at most O(N) (if the length of the array is N),
# in the worst case the pivot will divide the array to N-1 list and 1 list each time,
# and this will lead to Time Complexity of O(N^2), but in average will be if the pivot will be
# chosen as something at clos to the mean, and then we will get Time Complexity of O(Nlog(N))

# 2 - Analyze the space complexity of the recursive programs you implemented earlier.

# Factorial - the function will keep running until num<=2 and in each call we just subtract 1 from num,
# so it will be like one loop iterating over N (N=num) so the Time Complexity will be O(N).

# Permutations - the base case will give O(1) because it is a basic process, the for loop iterates over all the string,
# so it will give O(N) (N length of the string), then we have the nested for loop, in each recursive call there will be
# n function calls (n length of current string) and in each call the string length gets smaller with one letter
# so the nested loop will give us O(N!), and the total Time Complexity will be O(N*N!).
