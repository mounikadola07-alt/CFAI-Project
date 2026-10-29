## 2024-03-24 - DoS Vulnerability in O(N^2) Operations
**Vulnerability:** Unrestricted length of user input lists could cause Denial of Service (DoS) due to O(N^2) complexity of operations like building a Binary Search Tree (BST) from pre-sorted data.
**Learning:** Parsing arbitrarily long lists allows attackers to exhaust server resources when downstream operations (e.g. `build_bst`) have bad worst-case time complexities. The application hung on a request with 30,000 numbers because `build_bst` was O(N^2) for sorted arrays.
**Prevention:** Implement input length validation (e.g., maximum 15,000 elements) in parsing utilities like `validate_number_list` to bound the worst-case execution time of downstream functions.
