# Problem Statement: Secure My Conversation by Encryption and Decryption

# Person A and B use an encryption-based system for their conversation.

# Each conversation message is encrypted from the source and decrypted in the destination using a shared private positive number key known to each other.

# The algorithm is illustrated with an example.

# Input format with explanation:

# Operation (1 for Encryption and 2 for Decryption)
# Input message
# Input private key
# Output format with explanation:

# Output message
# Example 1:

# Input:

# 1
# Open
# 123
# Output:

# Oppeeen
# Here, the input message characters are duplicated based on each digit in the key.

# Example 2:

# Input:

# 2
# Oppeeen 
# 123
# Output:

# Open


import math
def get_key_list(key):
    f=[]
    while key!=0:
        remains=key%10
        key=key//10
        f.append(int(remains))
    return f


def operation_encrypt(msg, key):
    e_msg=''
    f=get_key_list(key)[::-1]
    l=min(len(msg),len(f))
    for i in range(l):
        e_msg = e_msg + msg[i] * f[i]
    if len(msg) > len(f):
        e_msg = e_msg + msg[l:]
    return e_msg

msg='open'
key=123
e_msg=operation_encrypt('open',123)

msg='oppeeen'
key=123
def operation_decrypt(msg, key):
    e_msg = ''
    f = get_key_list(key)[::-1]
    for i in range(len(f)):
        e_msg=e_msg+msg[sum(f[:i+1])-1:sum(f[:i+1])]
    if len(msg) > len(f):
        e_msg=e_msg+msg[sum(f[:]):]
    return e_msg
