
def sequence():
    seq = "AATCGGATTCCCG"
    count_A = 0
    count_G = 0
    count_C = 0
    count_T = 0
    count_AT = 0
    count_CG = 0

    # countA = seq.count("A")

    for char in seq:
        if char in ['A']:
            count_A += 1
        elif char in ['G']:
            count_G += 1
        elif char in ['T']:
            count_T += 1
        elif char in ['C']:
            count_C += 1
        elif char in ['AT']:
            count_AT += 1
        elif char in ['CG']:
            count_CG

    ATGC_Count = { "A":count_A,
                   "G":count_G,
                   "T":count_T,
                   "C":count_C,
                   "AT":count_AT,
                   "CG":count_CG,

    } # creating dict: key, value pair
    return ATGC_Count


def main():
    result = sequence()
    print(result)

if __name__ == "__main__":
    main()