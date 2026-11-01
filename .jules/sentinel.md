## 2026-11-01 - Input Validation Length Limit for DoS Prevention
**Vulnerability:** A Denial of Service (DoS) vulnerability existed in the `/api/search` endpoint where providing a very large sorted array could cause $O(N^2)$ time complexity during the Binary Search Tree (BST) creation step.
**Learning:** This existed because the `validate_number_list` function did not enforce a maximum length on the parsed integer list, allowing arbitrary-sized inputs from the user to reach computationally expensive internal functions.
**Prevention:** Always enforce a reasonable maximum length on user-provided arrays/lists during input validation to prevent resource exhaustion from poorly scaling downstream operations.
