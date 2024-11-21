def cipher(message):
    if message == "":
        print("Exiting...")
        exit()
    shift = int(input("Enter the shift value: "))
    ciphertext=""
    for ch in message:
        if ch>='a' and ch <='z':
            pos=ord(ch)-ord('a')
            new_pos= (pos + shift) % 26
            ch_new=chr(new_pos + ord('a'))
            ciphertext += ch_new
        elif ch >= 'A' and ch <= 'Z':
            pos = ord(ch) - ord('A')
            new_pos = (pos + shift) % 26
            ch_new = chr(new_pos + ord('A'))
            ciphertext += ch_new
        else:
            ciphertext += ch
    print(f"The cipher text is {ciphertext}")
def main():
    while True:
        m=input("Enter the message: ")
        cipher(m)
if __name__=="__main__":
    main()