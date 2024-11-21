import random

def generate_password():

    password_length = random.randint(7, 10)
    ascii_values = list(range(33, 127))
    password = []
    for _ in range(password_length):
        ascii_value = random.choice(ascii_values)
        ascii_values.remove(ascii_value)
        password.append(chr(ascii_value))
    return ''.join(password)

def main():

    num_times = int(input("Enter the number of times to generate the password: "))
    for _ in range(num_times):
        print(generate_password())

if __name__ == "__main__":
    main()