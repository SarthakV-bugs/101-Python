
input_bits = input("Enter 8 bits (0s and 1s): ")

if len(input_bits) != 8:
    print("Error: Input must be 8 bits")
else:
    num_ones = 0
    for bit in input_bits:
        if bit == '1':
            num_ones += 1


    if num_ones % 2 == 0:
        print("Parity bit: 0 (even parity)")
    else:
        print("Parity bit: 1 (odd parity)")
