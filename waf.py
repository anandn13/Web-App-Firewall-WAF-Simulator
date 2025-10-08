import re
from ml_model import predict_attack

PATTERNS = {
    "SQLi": re.compile(r"(?:')|(?:--)|(/\*(?:.|\n|\r)*?\*/)|"
                       r"\b(select|update|insert|delete|drop|exec|union|create|alter|cast)\b", re.IGNORECASE),
    "XSS": re.compile(r"(<script.*?>.*?</script>)|((javascript:)?alert\s*\()", re.IGNORECASE),
}

def regex_detect(payload: str):
    for attack, pattern in PATTERNS.items():
        if pattern.search(payload):
            return attack
    return None

def waf_check(payload: str):
    result = regex_detect(payload)
    if result:
        return result
    # ML fallback
    ml_result = predict_attack(payload)
    return ml_result if ml_result != "Normal" else None