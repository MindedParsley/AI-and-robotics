def encrypt(code, seed):
    encryptedString = ""
    for i in range(len(code)):
        encryptedString += chr( (ord( code[i] ) + seed) % 256 )
    print(encryptedString)
    return encryptedString

def decrypt(code, seed):    
    decryptedString = ""
    for i in range(len(code)):
            decryptedString += chr(( ord( code[i] ) - seed) % 256 )
    return decryptedString