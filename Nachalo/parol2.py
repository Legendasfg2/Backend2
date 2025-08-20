import random
import string

issued_tokens = []


def generate_unique_token(length=16):
    chars = string.ascii_letters + string.digits
    while True:
        token = "".join(random.choices(chars, k=length))
        if token not in issued_tokens:
            issued_tokens.append(token)
            return token
