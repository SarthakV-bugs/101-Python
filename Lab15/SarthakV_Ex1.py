#Create a program that reads a letter of the alphabet from the user.
#work on the possible error conditions

char=str(input("Enter the Alphabet: "))

if char in {"a", "e", "i" , "o" , "u", "A", "E", "I", "O", "U"}:
	print ("Entered letter is a vowel")
elif char=="y" or char=="Y":
	print ("Sometimes y/Y is a vowel and sometimes it is a consonant")
else:
	print ("consonant")

