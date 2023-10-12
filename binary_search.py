def binary_search(arr, x):
    """
    Perform binary search to find the index of element x in arr.
    
    :param arr: List[int], Sorted list of integers.
    :param x: int, Element to search for.
    :return: int, Index of element x in arr if found, otherwise -1.
    """
    
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

# Testing the function
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 7
    result = binary_search(arr, x)
    
    if result != -1:
        print(f"Element {x} is present at index {result}.")
    else:
        print(f"Element {x} is not present in array.")
