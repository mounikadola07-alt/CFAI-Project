## 2026-10-15 - [CRITICAL] Fix Flask debug mode enabled in production
**Vulnerability:** A Flask app appeared to be run with `debug=True`, which exposes the Werkzeug debugger and allows the execution of arbitrary code (CWE-94).
**Learning:** The application initialized Flask with a hardcoded `debug=True` flag in the `__main__` execution block. This could potentially allow arbitrary code execution if deployed to production. Also, general exceptions exposed internal details.
**Prevention:** Avoid hardcoding `debug=True`. Use environment variables to determine the execution environment and dynamically set the debugging flag. Also avoid exposing string versions of Exceptions to users in HTTP responses.
