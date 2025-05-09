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
