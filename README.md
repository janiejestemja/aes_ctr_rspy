## Requirements
---
- Python 3.12
- Rust (via [rustup.rs](https://rustup.rs))
- maturin (PyPI)

## Installing dependencies
---
```bash
pip install -r requirements.txt
```

## Building the wheel
---
```bash
maturin build --release
```
The wheel will be in target/wheels/, installable per pip via 
```bash
pip install target/wheels/*.whl
```

## Usage (/demo/...)
---
### Outdated usage (legacy)
---
```python
from aes_ctr_rspy import aes_ctr_py as aesify

data = b"Hello, world!"
key = b"0" * 32 
nonce = b"0" * 8 

encrypted = aesify(data, key, nonce)
decrypted = aesify(encrypted, key, nonce)

print(decrypted)
```
Should print *b'Hello, world!'* 

### Intended usage (current)
---
*/demo/usage.py*
```python
from aes_ctr_rspy import AesCtrSecret

key = bytearray(("2" * 32).encode())
nonce = bytearray(("4" * 8).encode())
secret = AesCtrSecret(key, nonce)

data = bytearray("This is a little longer test message than usual, to check if CTR is working as intended...".encode())
print("Plaintext: ", data, "\n")

ciphertext = bytearray(secret.encrypt(data))
print("Ciphertext: ", ciphertext, "\n")

key = bytearray(("2" * 32).encode())
nonce = bytearray(("4" * 8).encode())
secret2 = AesCtrSecret(key, nonce)

deciphered = secret2.encrypt(ciphertext)
print("Deciphered text: ", deciphered)
```

*Expected output*
```plaintext
Plaintext:  bytearray(b'This is a little longer test message than usual, to check if CTR is working as intended...') 

Ciphertext:  bytearray(b'...') 

Deciphered text:  b'This is a little longer test message than usual, to check if CTR is working as intended...'
```

*Note*: The AesCtrSecret struct overwrites the Python ByteArray passed as arguements to it, and zeroizes corresponding memory in Rust, thus has to be initialized/constructed for every encryption/decryption cycle.

### Known plaintext attack
---
If two messages use the same key and nonce
```plaintext
cipher1 = plaintext1 XOR keystream
cipher2 = plaintext2 XOR same_keystream
```

Then
```plaintext
cipher1 XOR cipher2 = plaintext1 XOR plaintext2
```

Can be thought of in Python like
```python
def xor_bytes(a, b):
    return bytearray(x ^ y for x, y in zip(a, b))

# Encrypt data1 and data2
ciphertext1 = bytearray(secret.encrypt(data1))
ciphertext2 = bytearray(secret.encrypt(data2))

# XOR ciphertexts
xored_ciphers = xor_bytes(ciphertext1, ciphertext2)

# Given data2 recover data1
recovered = xor_bytes(xored_ciphers, data2)
# Given data1 recover data2
recovered2 = xor_bytes(xored_ciphers, data)
```

*Take a look at /demo/kpa.py for more details...*

## License
---
MIT License.
