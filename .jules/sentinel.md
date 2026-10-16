## 2024-10-16 - DoS Vulnerability in BST Builder
**Vulnerability:** A Denial of Service (DoS) vulnerability existed in the `/api/search` endpoint where excessively long input arrays could exhaust server resources during the O(N^2) Binary Search Tree construction (when the array is pre-sorted before BST creation).
**Learning:** The lack of input length limits for user-provided data allowed attackers to force the server into performing computationally expensive operations, tying up resources.
**Prevention:** Always enforce reasonable maximum limits on user input data length, especially before passing that data into complex algorithms with super-linear time or space complexities.
