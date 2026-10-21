## 2024-10-21 - Algorithmic Complexity DoS in BST Builder
**Vulnerability:** A Denial of Service (DoS) vulnerability existed in the `/api/search` endpoint because `validate_number_list` did not restrict the size of the input array. Building a Binary Search Tree (BST) from pre-sorted arrays exhibits O(N^2) complexity, meaning large arrays (e.g., 50,000 items) took excessive time (~52 seconds) and CPU resources.
**Learning:** O(N^2) algorithms on user-provided input without bounds checking can easily lead to resource exhaustion and DoS.
**Prevention:** Always enforce reasonable length constraints on user-provided arrays or strings, especially before feeding them into computationally expensive algorithms.
