## 2024-10-14 - Fix Algorithmic Complexity DoS in BST
**Vulnerability:** The application was vulnerable to an Algorithmic Complexity Denial of Service (DoS) due to building a Binary Search Tree (BST) from an already-sorted array using a naive sequential insertion algorithm. This led to O(N^2) complexity and extremely deep, unbalanced trees, blocking the single-threaded server.
**Learning:** Naive BST insertion of pre-sorted data causes worst-case performance degradations, which can easily be exploited by user-supplied input to perform DoS.
**Prevention:** Always build a balanced BST from sorted data recursively (choosing the middle element as the root), achieving O(N) complexity and preventing degenerate trees.
