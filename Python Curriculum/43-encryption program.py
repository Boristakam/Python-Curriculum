import random
import string

""" string of characters that can be used to generate a random string, password, or encryption key """
chars_list = " " + string.punctuation + string.digits + string.ascii_letters
print(chars_list)
chars_list = list(chars_list) # creating a list of those characters

""" key list is a random copy of chars_list """
key = chars_list.copy() 
random.shuffle(key)

#print(f"chars_list: {chars_list}")
#print(f"key: {key}")


""" encryption """
plain_text = input("enter text to be encrypted: ")
encrypted_text = ""

for letter in plain_text:
    index = chars_list.index(letter)   #using index function to find the position of specific chars within the charslist. then adding the key at the same index to the encrypted msg
    encrypted_text += key[index]          #NOTE: you cannot use the append function to add to a string, throws an attributeerror

print(f"original message: {plain_text}")
print(f"encrypted message: {encrypted_text}")


""" decryption. to test it copy the encrypted message from the above block into the encryted text here """
encrypted_text = input("enter encrypted text: ")
plain_text = ""

for letter in encrypted_text:
    index = key.index(letter)  
    plain_text += chars_list[index]         

print(f"original message: {encrypted_text}")
print(f"encrypted message: {plain_text}")