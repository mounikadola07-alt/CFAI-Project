## 2026-10-12 - Prevent DoS via Large Payload parsing
**Vulnerability:** The application was susceptible to Denial of Service (DoS) due to unbounded parsing of arrays and strings on POST endpoints `/api/search` and `/api/subset`. Attackers could submit massive payloads, causing out-of-memory or high CPU utilization when splitting strings or evaluating `O(N^2)` algorithms.
**Learning:** This existed because the input validation utility (`validate_number_list`) lacked length or size validation limits.
**Prevention:** Always enforce upper bounds on input sizes, string lengths, and array elements before performing heavy computational work or parsing logic.
