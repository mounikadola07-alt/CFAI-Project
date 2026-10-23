## 2026-10-23 - Add array length limit for O(N^2) DoS mitigation
**Vulnerability:** The application was vulnerable to a Denial of Service (DoS) attack where a large, sorted list sent to the `/api/search` endpoint would cause excessive computation time due to the O(N^2) complexity of building a Binary Search Tree (BST) from pre-sorted data without balancing.
**Learning:** Even if individual algorithms are O(N) or O(log N), setup operations (like `build_bst` for unbalanced trees) can silently introduce O(N^2) complexities. Unbounded input length allows attackers to trigger these edge cases easily.
**Prevention:** Always set maximum input lengths (`max_length`) for API endpoints processing arrays, especially when the input flows into operations with worst-case non-linear complexity.
