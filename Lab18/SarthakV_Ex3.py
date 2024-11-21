def Cap_string(s):

        s = s.split()
        s[0] = s[0].capitalize()
        for i in range(1, len(s)):
            if s[i - 1][-1] in ['.', '!', '?']:
                s[i] = s[i].capitalize()
            elif s[i] == 'i':
                s[i] = 'I'
        return ' '.join(s)



def main():
    line = str(input("Enter the string to be capitalized: "))
    cap_string = Cap_string(line)
    print(cap_string)






if __name__ == "__main__":
      main()