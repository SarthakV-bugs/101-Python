import json

Morse_code={"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
"G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
"M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
"S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
"Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
"4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
"9": "----.", "0": "-----", ".": ".-.-.-", ",": "--..--", "?": "..--..",
"'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
"&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
"-": "-....-", "_": "..--.-", "$": "...-..-", "@": ".--.-."}

# a.
with open('morsefiles.json','w') as f:
    json.dump(Morse_code,f,indent=4)
with open('morsefiles.json','r') as f:
    print(json.load(f))


# b.
with open('sample.json', 'r') as f:
    morseDict=json.load(f)
    for row in morseDict:
        print(row.keys())
        print(row.values())
        print()
    for row in morseDict:
        if row['name']=="Bhupesh Menon":
            print(row['language'])
            break
