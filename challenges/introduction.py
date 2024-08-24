import sys
import pwn

def f2():
	if sys.version_info.major == 2:
		print("You are running Python 2, which is no longer supported. Please update to Python 3.")

	ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

	print("Here is your flag:")
	print("".join(chr(o ^ 0x32) for o in ords))


def f3():
	host = "socket.cryptohack.org"
	port = 11112
	r = pwn.remote(host, port)
	print(r.readline())
	print(r.readline())
	print(r.readline())
	print(r.readline())
	r.sendline('{"buy":"flag"}')
	print(r.readline())

f3()