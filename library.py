

alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
		   "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

rot13 = {"A": "N", "B": "O", "C": "P",	"D": "Q", "E": "R", 
		 "F": "S", "G": "T", "H": "U", "I": "V", "J": "W", 
		 "K": "X", "L": "Y", "M": "Z"}

rot18 = rot13

for x in range(10):
	if x+5 >= 10:
		rot18[str(x)] = str((x+5)%10)
	else:
		rot18[str(x)] = str(x+5)

numbers = {}

for x in range(len(alfabet)):
	numbers[alfabet[x]] = x+1

rot47 = {
    ' ': '!',
    '!': '"', '"': '#', '#': '$', '$': '%', '%': '&', '&': "'", "'": '(', '(': ')', ')': '*', '*': '+',
    '+': ',', ',': '-', '-': '.', '.': '/', '/': '0', '0': '1', '1': '2', '2': '3', '3': '4', '4': '5',
    '5': '6', '6': '7', '7': '8', '8': '9', '9': ':', ':': ';', ';': '<', '<': '=', '=': '>', '>': '?',
    '?': '@', '@': 'A', 'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I',
    'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S',
    'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': '[', '[': '\\', '\\': ']',
    ']': '^', '^': '_', '_': '`', '`': 'a', 'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g',
    'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q',
    'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': '{',
    '{': '|', '|': '}', '}': '~', '~': ' '
}

def translateToROT13(phrase):
	phrase = phrase.upper()
	translatedPhrase = ""
	for word in phrase:
		letter = "".join(word)
		if letter == " ":
			translatedPhrase += " "
		if letter in rot13.keys():
			key = rot13.get(letter)
			translatedPhrase += key
		else:
			for i in rot13:
				if rot13[i] == word:
					translatedPhrase +=i

	return translatedPhrase.lower()

def translateToNumbers(phrase):
	phrase = phrase.upper()
	translatedPhrase = ""
	for word in phrase:
		letter = "".join(word)
		if letter in numbers.keys():
			key = numbers.get(letter)
			if key < 10:
				key = "0" + str(key)
				translatedPhrase += key + "-"

			else:
				translatedPhrase += str(key) + "-"

	return translatedPhrase[:len(translatedPhrase)-1]

def translateToROT18(phrase):
	phrase = phrase.upper()
	translatedPhrase = ""
	for word in phrase:
		letter = "".join(word)
		if letter == " ":
			translatedPhrase += " "
		if letter in rot18.keys():
			key = rot18.get(letter)
			translatedPhrase += key
		else:
			for i in rot18:
				if rot18[i] == word:
					translatedPhrase+=i

	return translatedPhrase

def translateToROT47(phrase):

	encrypted_message = []

	for char in phrase:
		if char in rot47:
			encrypted_message.append(rot47[char])
		else:
			encrypted_message.append(char)

	return "".join(encrypted_message)