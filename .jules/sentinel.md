## 2024-11-06 - Prevent DoS from O(N^2) / complex operations
**Vulnerability:** The application was vulnerable to Denial of Service (DoS) due to unbounded input lists being processed by algorithms with O(N^2) or O(N log N) complexity, such as building a BST or comparing lists.
**Learning:** The lack of a maximum input length on user-supplied data allows an attacker to cause excessive CPU usage and application hang by submitting extremely large lists.
**Prevention:** Implement and enforce a sensible maximum length limit on input parsing functions (e.g., `validate_number_list`) to prevent excessive memory and CPU consumption.
