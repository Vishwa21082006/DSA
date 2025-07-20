Searching Algorithms in DSA

This repository contains implementations and explanations of fundamental **searching algorithms** used in Data Structures and Algorithms (DSA). Searching is an essential concept in computer science, used to locate a specific element in a data structure like an array, list, or tree.

---

Algorithms Included

| Algorithm              | Description                                               | Works on Sorted Data |
|------------------------|-----------------------------------------------------------|----------------------|
| Linear Search          | Searches element one by one                               | ❌                   |
| Binary Search          | Divides sorted array into halves to find element          | ✅                   |
| Jump Search            | Jumps ahead by fixed steps, then linear search            | ✅                   |
| Exponential Search     | Doubles the range until target found, then binary search  | ✅                   |
| Interpolation Search   | Uses interpolation formula to guess the position          | ✅                   |

---

Algorithm Details

### 1. Linear Search
- Time Complexity: **O(n)**
- Space Complexity: **O(1)**
- Best For: Small or unsorted arrays

### 2. Binary Search
- Time Complexity: **O(log n)**
- Space Complexity: **O(1)**
- Best For: Sorted arrays

### 3. Jump Search
- Time Complexity: **O(√n)**
- Space Complexity: **O(1)**
- Best For: Sorted arrays

### 4. Exponential Search
- Time Complexity: **O(log i)** where *i* is the position of the target
- Space Complexity: **O(1)**
- Best For: Unbounded or large sorted arrays

### 5. Interpolation Search
- Time Complexity: Best: **O(log log n)**, Worst: **O(n)**
- Space Complexity: **O(1)**
- Best For: Uniformly distributed sorted arrays

---

## 📂 Project Structure

