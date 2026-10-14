import time

def time_it(func):
    """
    A decorator that prints the execution time for the decorated function.
    We will use this later to measure our algorithms.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    return wrapper

# --- Error Handling Utilities ---
def validate_number_list(input_string):
    """
    Parses a string into a list of integers.
    Raises ValueError if invalid or empty.
    """
    if not input_string or not input_string.strip():
        raise ValueError("Input cannot be empty. Please provide a valid list of numbers.")
    try:
        # Handles comma separated or space separated
        cleaned = input_string.replace(',', ' ').split()
        if not cleaned:
            raise ValueError("No valid numbers found in the input.")
        return [int(x) for x in cleaned]
    except ValueError as e:
        # Re-raise the custom message if it's already generated, otherwise generic message
        if "No valid numbers" in str(e):
            raise
        raise ValueError("Invalid format: Please provide only integer values separated by commas or spaces.")

# --- Search Algorithms (Skeletons) ---
@time_it
def linear_search(arr, target):
    """
    Performs a linear search on a list.
    Returns the index if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

@time_it
def binary_search(arr, target):
    """
    Performs a binary search on a SORTED list.
    Returns the index if found, else -1.
    """
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

@time_it
def hash_search(hash_table, target):
    """
    Performs a search using a hash table (dict).
    Returns the index if found, else -1.
    """
    return hash_table.get(target, -1)

# --- BST Algorithms ---
class TreeNode:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.left = None
        self.right = None

def build_bst(arr):
    """
    Builds a balanced BST from an array in O(N log N) time.
    Prevents Algorithmic Complexity DoS from O(N^2) unbalanced insertions
    while maintaining the BST property even for unsorted inputs.
    """
    if not arr:
        return None

    # Pair elements with their original indices and sort them
    sorted_items = sorted([(val, i) for i, val in enumerate(arr)], key=lambda x: x[0])

    def helper(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        val, original_index = sorted_items[mid]
        node = TreeNode(val, original_index)
        node.left = helper(left, mid - 1)
        node.right = helper(mid + 1, right)
        return node

    return helper(0, len(arr) - 1)

@time_it
def bst_search(root: TreeNode, target: int) -> int:
    """
    Performs a search on a Binary Search Tree.
    Returns the index if found, else -1.
    """
    curr = root
    while curr:
        if curr.val == target:
            return curr.index
        elif target < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return -1

# --- Subset Algorithms (Skeletons) ---
@time_it
def is_subset_list(collection_a, collection_b):
    """
    Checks if collection_a is a subset of collection_b using List logic O(N * M).
    """
    for item in collection_a:
        if item not in collection_b:
            return False
    return True

@time_it
def is_subset_set(collection_a, collection_b):
    """
    Checks if collection_a is a subset of collection_b using Set logic O(N + M).
    """
    set_a = set(collection_a)
    set_b = set(collection_b)
    return set_a.issubset(set_b)


