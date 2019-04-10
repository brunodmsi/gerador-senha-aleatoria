import random
import sys
import string

if len(sys.argv) > 1: value = int(sys.argv[1])
else: value = 10

passLength = value

def randomPass():
	pass_chars = string.ascii_letters + string.punctuation + string.digits
	return ''.join(random.choice(pass_chars) for i in range(passLength))

if __name__ == "__main__":
	print randomPass()
