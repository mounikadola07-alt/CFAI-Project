## 2026-10-20 - Limit array lengths to prevent DoS
**Vulnerability:** A Denial of Service (DoS) vulnerability allowed arbitrarily large arrays (e.g. stringified lists of huge lengths) to be parsed. This can cause high memory and compute consumption, particularly when generating a Binary Search Tree (BST) from pre-sorted lists, resulting in an O(N^2) operation.
**Learning:** `validate_number_list` function had no upper limit on the number of elements it processed, allowing unrestricted processing of user-supplied JSON payload inputs at `/api/search` and `/api/subset` endpoints.
**Prevention:** Always enforce a maximum size limit (`max_length`) when parsing or accepting dynamically sized collections from user input.
