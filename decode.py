#In this code we will only do the Decryption Part
import time

# By this we get the Encrypted Code which was given to user using Encode.py earlier
encrypted_code = input("Enter your Encrypted Code: ")
  
  
#Here we will make our own Conversion Chart for the Respective Letters
conversion_table_ka_code = {
    
    # I have used a simple logic for Key here. 
    # Same logic used in Encryption but here Letters will be reversed
    # Any Encrypted letter eg. C is equal to (Its Previous Letter)-1
    # So C now is equal to A. Rest alphabets will follow the same case
    # Below are Alphabets which are Uppercase
    'C': 'A', 'D': 'B', 'E': 'C', 'F': 'D', 'G': 'E', 'H': 'F',
    'I': 'G', 'J': 'H', 'L': 'I', 'L': 'J', 'M': 'K', 'N': 'L', 
    'O': 'M', 'P': 'N', 'Q': 'O', 'R': 'P', 'S': 'Q', 'T': 'R',
    'U': 'S', 'V': 'T', 'W': 'U', 'X': 'V', 'Y': 'W', 'Z': 'X', 
    'A': 'Y', 'B': 'Z',
  
    #Alphabets which are Lowercase
    'c': 'a', 'd': 'b', 'e': 'c', 'f': 'd', 'g': 'e', 'h': 'f',
    'i': 'g', 'j': 'h', 'l': 'i', 'l': 'j', 'm': 'k', 'n': 'l', 
    'o': 'm', 'p': 'n', 'q': 'o', 'r': 'p', 's': 'q', 't': 'r',
    'u': 's', 'v': 't', 'w': 'u', 'x': 'v', 'y': 'w', 'z': 'x', 
    'a': 'y', 'b': 'z',
}
  
# Now code for getting the converted output ie. "The Encrypted Code"
decrypted_code = ""

for x in range(0, len(encrypted_code)):
    if encrypted_code[x] in conversion_table_ka_code.keys():
        decrypted_code += conversion_table_ka_code[encrypted_code[x]]
    else:
        decrypted_code += encrypted_code[x]
  
# Printing our Encrypted code output (\n is used for new line)
print("Decrypting your Hidden Message...")
time.sleep(2)

print("\nUser's given Encrypted Code was: ", encrypted_code)
print("The Decrypted Code for it will be: ", decrypted_code)

print("\n------This code is made by Gibran Khan Tareen------")