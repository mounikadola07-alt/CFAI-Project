## 2024-10-19 - DoS via Unbounded Input in Search Endpoints
**Vulnerability:** Unbounded array inputs in `validate_number_list` could cause a Denial of Service (DoS) because functions like `build_bst` operate with O(N^2) complexity on large pre-sorted arrays.
**Learning:** Parsing user input without setting an upper bound on length or size opens up the application to resource exhaustion vulnerabilities, especially when processing that input involves expensive algorithmic operations.
**Prevention:** Implement and enforce a hard limit on the length of input collections, dropping requests immediately if they exceed safe boundaries.
