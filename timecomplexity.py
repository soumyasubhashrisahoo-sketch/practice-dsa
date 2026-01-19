#Time Complexity 
# it isn't a measure of how many seconds a program takes to run.
# Instead, it measures how the runtime of an algorithm increases as the size of the input data increases.
#--If I say "My sorting algorithm takes 2 seconds," that doesn't tell you if the code is good or if my computer is just fast.
#---Time Complexity measures steps, not seconds. It asks: “As $n$ (the number of items) gets bigger, how much harder does the CPU have to work?”
# Time complexity tells us the relationship between n  and the number of operations the CPU has to perform.
'''
Notation,    Name,           Description,                                                      Example
O(1),        Constant,       Time stays the same regardless of input size.                     Accessing an element in an array by index.
O(logn),     Logarithmic,    Time increases slowly; the input is usually halved each step.,    Binary Search.
O(n),        Linear,         Time increases proportionally to the input size.,                 Finding an item in an unsorted list (looping once).
O(nlogn),    Linearithmic,   Often seen in efficient sorting algorithms.,                      Merge Sort or Quick Sort.
O(n2),       Quadratic,      Time increases exponentially (n squared).,                        Nested loops (checking every pair in a list).
'''
=====================================================================================================================================================================================================

'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''
#easy 
#Example(1)
print("Hello World")
#the time complexity is constant: O(1) i.e. every time a constant amount of time is required to execute code, no matter which operating system or which machine configurations you are using. 
# Auxiliary Space: O(1)

=======================================================================================================================================================================================================
#example2
n = 8
for i in range(1, n + 1):
    print("Hello World !!!")
#time complexity is linear: O(n) i.e. every time, a linear amount of time is required to execute code.
#Auxiliary Space: O(1)

=================================================================================================================================================================================================================
#example 3
#the time complexity is  Logarithmic O(log n)
n = 8
i = 1
while i <= n:
    print("Hello World !!!")
    i *= 2

   Iteration,    Value of i,    Condition (i <= 8),   Action,                      New i (i * 2)
      1,             1,              1≤8 (True),      "Prints ""Hello World""",    1×2=2
      2,             2,              2≤8 (True),      "Prints ""Hello World""",    2×2=4
      3,             4,              4≤8 (True),      "Prints ""Hello World""",    4×2=8
      4,             8,              8≤8 (True),      "Prints ""Hello World""",    8×2=16
     End,            16,             16≤8 (False),    Loop Stops,                    -
     

'''Hello World !!!
Hello World !!!
Hello World !!!
Hello World !!!
'''
=================================================================================================================================================================================================

#example 4

n = 8
i = 2
for j in range(2,n+1):
    if(i >= n):
        break 
    print("Hello World !!!")   
    i *= i

'''
Hello World !!!
Hello World !!!
'''
Iteration,        j value,          i value,         Condition (i >= 8),     Action,                        New i (i * i)
   1,              2,                   2,                 2≥8 (False),        "Prints ""Hello World"""     2×2=4
   2,              3,                   4,                 4≥8 (False),        "Prints ""Hello World""",    4×4=16
   3,              4,                   16,                16≥8 (True),         BREAKS LOOP,-

================================================================================================================================================================================================================

Q. Imagine a classroom of 100 students in which you gave your pen to one person. You have to find that pen without knowing to whom you gave it. 

Here are some ways to find the pen and what the O order is.
O(n2):You go and ask the first person in the class if he has the pen. Also, you ask this person about the other 99 people in the classroom if they have that pen and so on, 
This is what we call O(n2). 

O(n): Going and asking each student individually is O(N). 

O(log n): Now I divide the class into two groups, then ask: "Is it on the left side, or the right side of the classroom?" Then I take that group and divide it into two and ask again, and so on. 
Repeat the process till you are left with one student who has your pen. This is what you mean by O(log n). 


I might need to do:

The O(n2) searches if only one student knows on which student the pen is hidden. 
The O(n) if one student had the pen and only they knew it. 
The O(log n) search if all the students knew, but would only tell me if I guessed the right side

=========================================================================================================================================================================================================================================

Q1. Find the Sum of 2 numbers

a = 5
b = 6

def sum(a,b):
  return a+b

 # function call
print(sum(a,b))

#output 11
#Time Complexity = O(2) = O(1), since 2 is constant


=================================================================================================================================================================================================


Q2. Find the sum of all elements of a list/array
# A function to calculate the sum of the elements in an array
def list_sum(A, n):
    sum = 0
    for i in range(n):
        sum += A[i]
    return sum


# A sample array
A = [5, 6, 1, 2]

# Finding the number of elements in the array
n = len(A)

# Call the function and print the result
print(list_sum(A, n))

#Output14

'''the time complexity of the above code is O(n)+'''