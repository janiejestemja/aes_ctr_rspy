## aes_ctr_rspy
---
> AES CTR 256 bits encryption written in Rust & compiled to Python extension. 

## Installation
---
> Requires `Python 3.12`

Download Asset from latest release on github.

Setup a venv and install the downloaded wheel via pip...
```python
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install Downloads/aes_ctr_rspy*.whl
```

## Example usage
---

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

--

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


## Developer notes...
---
> Building from source

### Requirements
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

## License
---
MIT License.
