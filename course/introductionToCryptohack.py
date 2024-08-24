#!/usr/bin/env python3
import sys
import base64
from Crypto.Util.number import *
import pwn

def f1():
	if sys.version_info.major == 2:
		print("You are running Python 2, which is no longer supported. Please update to Python 3.")

	ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

	print("Here is your flag:")
	print("".join(chr(o ^ 0x32) for o in ords))

def f2():
	ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
	print("".join(chr(o) for o in ords))

def f3():
	hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
	print(bytes.fromhex(hex).decode("utf-8"))

def f4():
	hex_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
	hex = bytes.fromhex(hex_str)
	base64_str = base64.b64encode(hex)
	print(base64_str.decode("utf-8"))

def f5():
	integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
	print(long_to_bytes(integer).decode("utf-8"))

def f6():
	print("crypto{"+pwn.xor("label", 13).decode("utf-8")+"}")

def f7():
	'''
	Commutative: A ⊕ B = B ⊕ A
	Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
	Identity: A ⊕ 0 = A
	Self-Inverse: A ⊕ A = 0
	'''
	
	k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
	k1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
	k2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
	flag_k1_2_3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

	k2 = pwn.xor(bytes.fromhex(k1), bytes.fromhex(k1_2))
	k3 = pwn.xor(k2, bytes.fromhex(k2_3))
	k_1_2_3 = pwn.xor(bytes.fromhex(k1_2), k3)
	flag = pwn.xor(k_1_2_3, bytes.fromhex(flag_k1_2_3))
	print(flag)

def f8():
	k = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
	for i in range(256):
		print(pwn.xor(bytes.fromhex(k), i), i)

def f9():
	k = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
	decoded = bytes.fromhex(k)
	partialKey = pwn.xor(decoded[:7], 'crypto{').decode() + 'y'
	complete_key = (partialKey * (len(decoded)//len(partialKey)+1))[:len(decoded)]

	flag = pwn.xor(complete_key, decoded)
	print(flag)
	
f9()
