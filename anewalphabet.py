alphabet = {"a": "@", "n": "[]\[]", "b": "8", "o": "0", "c": "(", "p": "|D",
			"d": "|)", "q": "(,)", "e": "3", "r": "|Z", "f": "#", "s": "$", "g": "6",
			"t": "']['", "h": "[-]", "u": "|_|", "i": "|", "v": "\/", "j": "_|", "w": "\/\/",
			"k": "|<", "x": "}{", "l": "1", "y": "`/", "m": "[]\/[]", "z": "2",}
string = input().lower()
output = ""
for letter in string:
	try:
		output += alphabet[letter]
	except:
		output += letter
print(output)