import hashlib
import random
import string

def generate_checksum(params, merchant_key):
    params_string = ''
    for key in sorted(params.keys()):
        value = str(params[key])
        params_string += f"{key}:{value}|"
    params_string += f"key:{merchant_key}"
    return hashlib.sha256(params_string.encode()).hexdigest()

def verify_checksum(params, merchant_key, checksum):
    generated = generate_checksum(params, merchant_key)
    return generated == checksum

# Optional: for generating dummy order ID
def __time_stamp__():
    return ''.join(random.choices(string.digits, k=6))
