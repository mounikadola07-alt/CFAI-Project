## 2025-02-25 - Prevent DoS via Large Inputs to O(N^2) Operations
**Vulnerability:** Found a potential Denial of Service (DoS) vulnerability where very large arrays could be passed to endpoints (e.g., `/api/search`) which perform operations that don't scale well (like building a BST from pre-sorted data, taking O(N^2) time).
**Learning:** The `validate_number_list` function had no upper bound on the number of elements it processed. This allowed attackers to submit arbitrarily large payloads that would exhaust server resources (CPU/Memory).
**Prevention:** Added a `max_length` parameter (defaulting to 15000) to `validate_number_list` to enforce a hard limit on input size before expensive processing occurs.
