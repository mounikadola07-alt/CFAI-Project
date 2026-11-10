## 2024-05-18 - Flask Werkzeug Debugger RCE
**Vulnerability:** Running Flask app with `debug=True` in production can expose the Werkzeug interactive debugger, leading to Remote Code Execution (RCE).
**Learning:** The development server config was pushed to the main file, enabling a severe security loophole that should strictly be confined to local dev instances.
**Prevention:** Always set `debug=False` or omit it in production. Use environment variables (e.g. `FLASK_ENV=development`) for enabling debug modes locally instead of hardcoding.

## 2024-05-18 - O(N^2) DoS in BST construction
**Vulnerability:** Building a BST from pre-sorted arrays takes O(N^2) time. Lack of input length restrictions enabled a Denial of Service (DoS) attack where massive lists could hang the server.
**Learning:** Algorithm complexities, especially worst-case O(N^2) paths, can easily become a vector for DoS if untrusted user input scales unbounded.
**Prevention:** Always implement sensible `max_length` validations for collections derived from user input, specifically before performing computationally expensive operations.
