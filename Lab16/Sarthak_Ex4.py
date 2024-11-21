
def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


word=input(str("Enter the string that you want to check: ")).lower()
ans = isPalindrome(word)

if (ans):
    print("Yes")
else:
    print("No")