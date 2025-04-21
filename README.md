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

## Usage
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

```python
from aes_ctr_rspy import AesCtrSecret

key = bytearray(("2" * 32).encode())
nonce = bytearray(("4" * 8).encode())
secret = AesCtrSecret(key, nonce)

print("Key: ", key)
print("Nonce: ", nonce)

data = bytearray("This is a little longer test message than usual, to check if CTR is working as intended...".encode())
print(data)

ciphertext = bytearray(secret.encrypt(data))

key = bytearray(("2" * 32).encode())
nonce = bytearray(("4" * 8).encode())
secret2 = AesCtrSecret(key, nonce)

deciphered = secret2.encrypt(ciphertext)
print(deciphered)
```

*Note*: The AesCtrSecret struct overwrites the Python ByteArray passed as arguements to it, and zeroizes corresponding memory in Rust, thus has to be initialized for every encryption/decryption cycle.

## License
---
MIT License.
