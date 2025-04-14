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
The wheel will be in target/wheels/

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
