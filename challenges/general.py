import base64
from Crypto.Util.number import *
import pwn

def f1():
	ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
	decrypted = ""
	for i in ascii:
		decrypted += str(chr(i))
	print(decrypted)

def f2():
	string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
	decoded = bytes.fromhex(string)
	print(decoded)

def f3():
	string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
	decoded = bytes.fromhex(string)
	frombase = base64.b64encode(decoded)
	print(frombase)

def f4():
	hex = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
	decoded = long_to_bytes(hex)
	print(decoded)

def f5():
	host = "socket.cryptohack.org"
	port = 13377
	r = pwn.remote(host, port)
	print(r.readline())

f5()