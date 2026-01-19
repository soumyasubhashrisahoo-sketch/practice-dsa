# Greedy Algorithm & Dynamic Programming

**Examples with Explanation (DSA using Python)**

---

# 1️⃣ Greedy Algorithm — Example

---

## Example Problem: Coin Change (Greedy Approach)

### Problem Statement

Given an amount and coin denominations, find the minimum number of coins required to make the amount using a greedy approach.

Coins = `[10, 5, 2, 1]`
Amount = `28`

---

## Diagram (Greedy Decision Flow)

```
Amount = 28
   |
Choose largest coin ≤ 28 → 10
   |
Remaining = 18
   |
Choose largest coin ≤ 18 → 10
   |
Remaining = 8
   |
Choose 5 → 2 → 1
```

---

## Explanation

The greedy algorithm:

* Always chooses the **largest possible coin**
* Does not reconsider previous choices
* Aims to minimize number of coins

This works correctly here because the coin system is **canonical**.

---

## Python Code (Greedy Coin Change)

```python
coins = [10, 5, 2, 1]
amount = 28

for coin in coins:
    while amount >= coin:
        print(coin, end=" ")
        amount -= coin
```

---

## Output

```
10 10 5 2 1
```

---

## Key Observation

✔ Fast and simple
❌ May fail for some coin systems

---

# 2️⃣ Dynamic Programming — Example

---

## Example Problem: Fibonacci Series (DP Approach)

### Problem Statement

Find the nth Fibonacci number using dynamic programming.

Fibonacci formula:

```
F(n) = F(n-1) + F(n-2)
```

---

## Diagram (Overlapping Subproblems)

```
F(5)
 |
 ├── F(4)
 |    ├── F(3)
 |    └── F(2)
 |
 └── F(3)   ← repeated subproblem
```

Dynamic Programming avoids recalculating `F(3)`.

---

## Explanation

Dynamic Programming:

* Breaks problem into smaller subproblems
* Stores results in a table
* Reuses stored values

This avoids repeated calculations and improves efficiency.

---

## Python Code (DP Fibonacci)

```python
def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print(fibonacci(6))
```

---

## Output

```
8
```

---

## Key Observation

✔ Always optimal
✔ Much faster than recursion
❌ Uses extra memory

---

# 3️⃣ Greedy vs Dynamic Programming (Example-Based Insight)

| Aspect   | Greedy     | Dynamic Programming |
| -------- | ---------- | ------------------- |
| Decision | Local best | Global best         |
| Memory   | Very low   | High                |
| Speed    | Very fast  | Moderate            |
| Accuracy | May fail   | Always correct      |

---

## Exam Tip ⭐

* Use **Greedy** when choices are independent
* Use **DP** when subproblems overlap

---

**END OF FILE**
