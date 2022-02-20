def encrypt(text,s): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        else: 
            result += chr((ord(char) + s-97) % 26 + 97) 
  
    return result 
def decrypt(cipher,s):
    original=""
    for i in range(len(cipher)):
        char = cipher[i]
        if (char.isupper()):
            original += chr((ord(char) - s+65) % 26 + 65 )
        else: 
            result += chr((ord(char) - s+97) % 26 + 97)
    
    return original
text = input("Enter text ")
s = int(input("Key "))
print ("Text  : " + text)
print ("Shift : " + str(s)) 
cipher = encrypt(text,s)
decrypting= decrypt(cipher,s)
print ("Cipher: " + cipher)
print ("Decrypted: " + decrypting)