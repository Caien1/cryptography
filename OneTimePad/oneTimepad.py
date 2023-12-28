import random
def genrateKey(length):
    charSet = "ABCDEFGHIJKLMNOPQRST"
    key = ""
    for i in range(length):
        key = key + random.choice(charSet)
    return key

def encrypt(plainText, key):
    offset = ord("A")
    cipherText = ""
    for i in range(len(plainText)):
        val = (ord(plainText[i])+ord(key[i])-2*offset)
        val = val%26 + offset
        cipherText +=chr(val)    
    return cipherText

def main():
    print("Enter plain text :",end =" ")
    plainText = input().upper().replace(" ","") #captilise and remove white spaces for easier processing
    key = genrateKey(len(plainText))
    cipherText = encrypt(plainText,key)
    print(f'Cipher text {cipherText}, key {key}')

main()
