def is_magic_date(day, month, year):

    two_digit_year = year % 100
    return day * month == two_digit_year


def find_magic_dates():
    magic_dates = []


    for year in range(1900, 2000):
        for month in range(1, 13):

            if month in [1, 3, 5, 7, 8, 10, 12]:
                num_days = 31
            elif month in [4, 6, 9, 11]:
                num_days = 30
            elif month == 2:  
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    num_days = 29
                else:
                    num_days = 28

            for day in range(1, num_days + 1):
                if is_magic_date(day, month, year):
                    magic_dates.append(f"{month:02}/{day:02}/{year}")

    return magic_dates


def main():
    magic_dates = find_magic_dates()
    print("Magic Dates in the 20th Century:")
    for date in magic_dates:
        print(date)


if __name__ == "__main__":
    main()
