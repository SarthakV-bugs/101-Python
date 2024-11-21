def keypad(text):
    #
    dict1 = {0: [' '],
        1: ['.', ',', '?', '!', ':'],
        2: ['A', 'B', 'C'],
        3: ['D', 'E', 'F'],
        4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'],
        6: ['M', 'N', 'O'],
        7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'],
        9: ['W', 'X', 'Y', 'Z']
    }

    output = []
    for i in text.upper():
            for key, values in dict1.items():
                if i in values:
                    x=values.index(i)+1
                    output.append(str(key) * x)

    return ''.join(output)


def main():
    text = input('Enter the text: ')
    print(keypad(text))




if __name__ == "__main__":
        main()
