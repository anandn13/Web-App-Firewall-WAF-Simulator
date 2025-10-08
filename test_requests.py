import requests

API_URL = "http://localhost:8000/waf/check"

payloads = [
    "SELECT * FROM users WHERE id = 1",
    "<script>alert('XSS')</script>",
    "Hello, world!",
    "admin' --",
    "<img src=x onerror=alert('XSS')>",
    "Welcome to the homepage.",
    "javascript:alert('XSS')"
]

for payload in payloads:
    res = requests.post(API_URL, json={"payload": payload})
    print(f"Payload: {payload} => Result: {res.json()['result']}")