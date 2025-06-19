# binary_search_dsa.py

from typing import List

def binary_search_iter(arr: List[int], target: int) -> int:
    """Iterative binary search: returns index of target or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_rec(arr: List[int], left: int, right: int, target: int) -> int:
    """Recursive binary search."""
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, mid + 1, right, target)
    else:
        return binary_search_rec(arr, left, mid - 1, target)

def main():
    # Example usage
    arr = sorted([15, 3, 9, 27, 1, 35, 7])
    target = int(input("Enter number to search: "))
    
    print(f"Sorted array: {arr}")
    
    idx_iter = binary_search_iter(arr, target)
    if idx_iter != -1:
        print(f"[Iterative] {target} found at index {idx_iter}")
    else:
        print(f"[Iterative] {target} not found")
    
    idx_rec = binary_search_rec(arr, 0, len(arr)-1, target)
    if idx_rec != -1:
        print(f"[Recursive] {target} found at index {idx_rec}")
    else:
        print(f"[Recursive] {target} not found")

if __name__ == "__main__":
    main()
