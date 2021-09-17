#In this code we will only do the Encrypting Part
import time

# By this we will get the Message which User wants to encrypt
user_ka_input = input("Enter your message: ")
  
  
# Here we will make our own Conversion Chart for the Respective Letters
# This Conversion Chart is also known as "KEY" for the Encryption
conversion_table_ka_code = {
    
    # I have used a simple logic for Key here. 
    # Any alphabel eg. A is equal to (Its Next Alphabet)+1
    # So A is equal to C, and so will follow the rest alphabets
    # Below are Alphabets which are Uppercase
    'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H',
    'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 
    'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T',
    'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 
    'Y': 'A', 'Z': 'B',
  
    #Alphabets which are Lowercase
    'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h',
    'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n',
    'm': 'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't',
    's': 'u', 't': 'v', 'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z',
    'y': 'a', 'z': 'b'
}
  
# Now code for getting the converted output ie. "The Encrypted Code"
encrypted_code = ""

for x in range(0, len(user_ka_input)):
    if user_ka_input[x] in conversion_table_ka_code.keys():
        encrypted_code += conversion_table_ka_code[user_ka_input[x]]
    else:
        encrypted_code += user_ka_input[x]
  
# Printing our Encrypted code output (\n is used for new line)
print("Encrypting...")
time.sleep(2)

print("\nUser's Given Message was: ", user_ka_input)
print("Now the New Encrypted Code will be: ", encrypted_code)

print("\n------This code is made by Gibran Khan Tareen------")