import hashlib
from arc4 import ARC4  
import binascii

file = open("89210AF9.bin","rb") #Resource with Qakbot configuration
resource = file.read()

key = hashlib.sha1(b"Muhcu#YgcdXubYBu2@2ub4fbUhuiNhyVtcd").digest()
rc4 = ARC4(key)
data = rc4.decrypt(resource)

key = data[20:40]
rc4 = ARC4(key)

decrypted_data = rc4.decrypt(data[40:])
print((decrypted_data[20:]).decode("utf-8"))