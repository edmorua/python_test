
def encrypt(encryp_key):
	password_int = input('Enter password: ')
	password_out = ''
	from_char = 0
	to_char = 1
	for ch in password_int:
		letter_found = False
		for t in encryp_key:
			if('a'<=ch and ch <= 'z') and ch == t[from_char]:
				password_out = password_out + t[to_char]
				letter_found = True
			elif('A'<= ch and ch <= 'Z') and chr(ord(ch) +32) == t[from_char]:
				password_out = password_out + chr(ord(t[to_char]) - 32)
				letter_found = True
		if not letter_found:
			password_out = password_out + ch
	print('Your encrypted password is:', password_out)

def decrypt(encryp_key):
	password_int = input('Enter password: ')
	password_out = ''
	from_char = 1
	to_char = 0
	for ch in password_int:
		letter_found = False
		for t in encryp_key:
			if('a'<=ch and ch <= 'z') and ch == t[from_char]:
				password_out = password_out + t[to_char]
				letter_found = True
			elif('A'<= ch and ch <= 'Z') and chr(ord(ch) +32) == t[from_char]:
				password_out = password_out + chr(ord(t[to_char]) - 32)
				letter_found = True
		if not letter_found:
			password_out = password_out + ch
	print('Your decrypted password is:', password_out)

def main():
	encryp_key = (('a','m'),('b','h'),('c','t'), ('d','f'),('e','g'),
			('f','k'),('g','b'),('h','p'),('i','j'),('j','w'),('k','e'),
			('l','r'),('m','q'),('n','s'),('o','l'),('p','n'),('q','i'),
			('r','u'),('s','o'),('t','x'),('u','z'),('v','y'),('w','v'),
			('x','d'),('y','c'),('z','a'),('_','*'),('*','#'),('#','$'),('$','_'))
	print("This program will encrypt and decrypt user passwords\n")
	select = input("Enter (e) to encrypt or (d) to decrypt: ")
	
	while select != 'e' and select != 'd':
		select = input("\nINVALID - Enter 'e' or 'd': ")
	if (select == 'e'):
		encrypt(encryp_key)
	else:
		decrypt(encryp_key)


if __name__ == '__main__':
	main()