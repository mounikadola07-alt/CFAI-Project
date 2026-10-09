## 2023-10-09 - Algorithmic Complexity DoS Vulnerability
**Vulnerability:** CPU exhaustion DoS via `build_bst` and unbounded input lengths.
**Learning:** The application sorts user input arrays before passing them to `build_bst`. For a standard BST insertion algorithm, providing a sorted array triggers the O(N^2) worst-case time complexity (creating a linked list). Combined with unrestricted input string lengths, an attacker could easily cause severe server delays with a relatively small payload.
**Prevention:** Always implement strict maximum length limits on user input (Defense in Depth) and be mindful of worst-case algorithmic complexities when designing operations on user-controlled data.
