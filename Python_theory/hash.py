def main():
    strings = ['abcdef', 'bcdefa','sarthak']
    p = [1, 2, 3, 4, 5, 6]
    hash_vals = []

    for s in strings:
        x = 0
        for j in range(len(s)):
            x += ord(s[j]) * p[j]
        hash_vals.append(x % 2069)

    print(hash_vals)

    s1 = 'abcdef'
    print(hash(s1))

if __name__ == "__main__":
    main()