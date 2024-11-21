from unittest.mock import sentinel


def capitalize_i(sent):
     for i in range(0,len(sent)):
         if sent[i] == 'i':
             sent[i]=sent[i].upper()
     return sent

















def main():
    s=input("Enter the sentence:")
    sent=list(s)
    print(capitalize_i(sent))


if __name__ == "__main__":
        main()
