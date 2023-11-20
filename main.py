import collections
import hashlib
import random
import rabbit 
import binascii
import sys


message=str(input("Nhap message: "))
key=str(input("Nhap key: "))
iv=0


key1 = hashlib.md5(key.encode()).hexdigest()


print("Message:\t\t",message)
print("IV:\t",iv)
print("Encryption password:\t",key)
print("Encryption key:\t\t",key1)
print("\n======Rabbit encryption========")

iv=0

msg=rabbit.Rabbit(key1,iv).encrypt(message)
print("Encrypted:\t",binascii.hexlify(msg.encode()))

text=rabbit.Rabbit(key1,iv).decrypt(msg)

print("Decrypted:\t",text)
