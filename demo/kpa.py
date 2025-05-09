from aes_ctr_rspy import AesCtrSecret

# Helper function
def xor_bytes(a, b):
    return bytearray(x ^ y for x, y in zip(a, b))

# (Re-)starting encryption engine (DRY)
def get_crypt_engine(key_var="1", nonce_var="1"):
    key = bytearray((key_var * 32).encode())
    nonce = bytearray((nonce_var * 8).encode())
    secret = AesCtrSecret(key, nonce)
    return secret

# Definition of data for example
data1 = bytearray("This is a little longer test message than usual, to check if CTR is working as intended...".encode())
data2 = bytearray("Other - shorter - message.".encode())

# Encrypting first text
secret = get_crypt_engine("2", "2")
ciphertext1 = bytearray(secret.encrypt(data1))

# Encrypting second text
secret = get_crypt_engine("2", "2")
ciphertext2 = bytearray(secret.encrypt(data2))

# XOR ciphertexts
xored_ciphers = xor_bytes(ciphertext1, ciphertext2)

# Given data or data2 respectively recover the other one
recovered1 = xor_bytes(xored_ciphers, data2)
recovered2 = xor_bytes(xored_ciphers, data1)

# Print out recovered messages
print("Broken: ")
print("First message: ", recovered1)
print("Other message: ", recovered2)
