# Algorithm Design Paradigms

**DSA using Python | Sem 2 – BTech CSE (AI & ML)**

---

## 1. What are Algorithm Design Paradigms?

Algorithm design paradigms are **general approaches** or **strategies** used to solve computational problems efficiently.

Instead of writing algorithms randomly, we **follow a paradigm**.

---

## 2. Main Algorithm Design Paradigms

1. Divide and Conquer
2. Greedy Method
3. Dynamic Programming

---

# 1️⃣ Divide and Conquer

---

## Concept

**Divide and Conquer** works by:

1. Dividing the problem into smaller subproblems
2. Solving each subproblem
3. Combining the results

---

## Diagram

```
Problem
   |
Divide
 /   \
Sub   Sub
 |     |
Solve Solve
   \   /
   Combine
```

---

## Explanation

* Big problem is broken into **similar smaller problems**
* Each subproblem is easier to solve
* Results are combined to get final answer

---

## Example (Real Life)

📘 Searching a word in a dictionary:

* Open middle page
* Decide left or right half
* Repeat

---

## Example (Algorithm)

### Binary Search (Classic Example)

```python
def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    return -1
```

---

## Key Points (Exam)

* Recursive in nature
* Efficient for large problems
* Time complexity often **O(n log n)**

---

# 2️⃣ Greedy Algorithm

---

## Concept

A **Greedy algorithm**:

* Makes the **best choice at each step**
* Does not think about future consequences

📌 “Take what looks best **right now**”

---

## Diagram

```
Start
  |
Best choice now
  |
Best choice now
  |
Final solution
```

---

## Explanation

* Chooses locally optimal solution
* Hopes local optimum → global optimum
* Simple and fast

---

## Example (Real Life)

💰 Giving change:

* Use highest currency note first
* Then next highest

---

## Example (Algorithm)

### Coin Change (Greedy)

```python
coins = [10, 5, 2, 1]
amount = 28

for coin in coins:
    while amount >= coin:
        print(coin, end=" ")
        amount -= coin
```

Output:

```
10 10 5 2 1
```

---

## Key Points (Exam)

* Easy to implement
* Faster than DP
* **May not always give optimal solution**

---

# 3️⃣ Dynamic Programming (DP)

---

## Concept

Dynamic Programming solves problems by:

* Breaking into **overlapping subproblems**
* Storing results to avoid recomputation

📌 “Solve once, reuse many times”

---

## Diagram

```
Problem
  |
Subproblem 1 ----\
  |               \
Store result       -> Use stored values
  |               /
Subproblem 2 ----/
```

---

## Explanation

* Uses **memory (table/array)**
* Avoids repeated calculations
* Very efficient for complex problems

---

## Example (Real Life)

📘 Studying formulas:

* Learn once
* Use many times in exam

---

## Example (Algorithm)

### Fibonacci using Dynamic Programming

```python
def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]
```

---

## Key Points (Exam)

* Uses extra space
* Faster than recursion
* Time complexity often **O(n)**

---

## 4️⃣ Comparison of Paradigms ⭐

| Paradigm            | Strategy          | Memory   | Example     |
| ------------------- | ----------------- | -------- | ----------- |
| Divide & Conquer    | Divide problem    | Low      | Merge Sort  |
| Greedy              | Best local choice | Very Low | Coin Change |
| Dynamic Programming | Store results     | High     | Fibonacci   |

---

## 5️⃣ When to Use What?

* **Divide & Conquer** → Independent subproblems
* **Greedy** → Fast approximation
* **Dynamic Programming** → Overlapping subproblems

---

## 6️⃣ Exam Short Definitions (2 Marks)

### Divide and Conquer

An algorithmic technique that divides a problem into smaller subproblems, solves them independently, and combines their results.

### Greedy Algorithm

An algorithm that makes the locally optimal choice at each step to reach a solution.

### Dynamic Programming

An algorithmic technique that solves problems by storing solutions to overlapping subproblems to avoid recomputation.

---

**END OF NOTES**
