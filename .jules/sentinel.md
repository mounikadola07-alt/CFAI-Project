## 2025-02-18 - Input Length Limit to Prevent DoS
**Vulnerability:** Unbounded user input was passed directly into O(N^2) algorithms (building BST from pre-sorted array) and subset checks (O(N * M)). Sending very large arrays could cause high CPU utilization, leading to a Denial of Service (DoS) condition.
**Learning:** Even simple utility functions like `validate_number_list` can become attack vectors if they don't bound the input sizes before passing them to more complex algorithms. It is crucial to define upper limits for input collections.
**Prevention:** Always enforce a reasonable `max_length` limit (or size limitation) on user-submitted collections/arrays before processing them, especially when they are processed by algorithms with O(N^2) or greater time complexity.
