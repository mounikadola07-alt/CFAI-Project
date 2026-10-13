## 2024-05-18 - Algorithmic DoS in BST Building
**Vulnerability:** Application allows a single request with a large input array (e.g., 30,000 items) to hang the server, because `build_bst` operates with $O(N^2)$ complexity on sorted or sequential array inputs.
**Learning:** Even though building a BST has $O(N \log N)$ expected time, sequentially inserting already-sorted data produces an unbalanced tree (a linked list), which takes $O(N^2)$ time. This algorithmic complexity gap allows a Denial of Service.
**Prevention:** Implement input length validation upstream before processing unbounded collections, and consider balancing trees (e.g., AVL, Red-Black) to guarantee worst-case logarithmic insertion if large sorted sets are expected.
