import hashlib

message = "ma chung thanh".encode()

print("MD5: ", hashlib.md5(message).hexdigest())

print("SHA- 256: ", hashlib.sha256(message).hexdigest())

print("SHA-512: ", hashlib.sha512(message).hexdigest())

print("SHA-128: ", hashlib.shake_128(message).hexdigest())