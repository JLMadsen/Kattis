n = int(input())
for i in range(n):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m" ,"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

	input_string =  input().lower()

	for letter in input_string:
		try:
			alphabet.remove(letter)
		except:
			f = 0

	if len(alphabet) == 0:
		print("pangram")
	else:
		missing = ""
		for remaining in alphabet:
			missing += remaining
		print("missing", missing)