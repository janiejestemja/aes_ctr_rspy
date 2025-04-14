from aes_ctr_rspy import AesCtrSecret

key = bytearray(b"2" * 32)
nonce = bytearray(b"4" * 8)
secret = AesCtrSecret(key, nonce)

print("Key: ", key)
print("Nonce: ", nonce)

data = bytearray(b"This is a little longer test message than usual, to check if CTR is working as intended...")
print(data)

ciphertext = bytearray(secret.encrypt(data))

key = bytearray(b"2" * 32)
nonce = bytearray(b"4" * 8)
secret2 = AesCtrSecret(key, nonce)

deciphered = secret2.encrypt(ciphertext)
print(deciphered)
