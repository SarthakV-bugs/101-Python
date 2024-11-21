from random import randint

def dice_rolls():
    rolls = []
    for i in range(1000):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        total = d1 + d2
        rolls.append(total)
    return rolls

def count_freq(roll_list):
    freq = {}
    for i in range(2, 13):
        freq[i] = roll_list.count(i)
    return freq

def main():
    rolls = dice_rolls()
    frequencies = count_freq(rolls)
    print("Frequencies:")
    for key in frequencies:
        print(key, ":", frequencies[key])

if __name__ == "__main__":
    main()
