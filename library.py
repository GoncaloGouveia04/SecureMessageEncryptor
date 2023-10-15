

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

rot47 = {}

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

def translateToRot18(phrase):
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