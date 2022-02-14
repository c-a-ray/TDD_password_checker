"""
Specifications:
    * Must be between 8 and 20 characters (inclusive)
    * Must contain at least one lowercase letter
    * Must contain at least one uppercase letter
    * Must contain at least one digit
    * Must contain at least one symbol from: ~`!@#$%^&*()_+-=
"""

def check_pwd(pwd: str) -> bool:
    pwd_len = len(pwd)
    return pwd_len >= 8 and pwd_len <= 20
