import random
from Encypt import decrypt,encrypt

code = input("enter a tring to encode: ")
seed = random.randint(1,255)

print(f"encrypted code: {encrypt(code,seed)}")
enCode = encrypt(code,seed)
print(f"decrypted code: {decrypt(enCode,seed)}")