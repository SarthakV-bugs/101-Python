
def is_magicdate(year, month , day ):

    two_digit_year = year % 100
    if month * day == two_digit_year:
        return True
    else:
        return False



def is_leapyear(year):

    if year % 400 == 0:
        return 29
    elif year % 4 == 0 and year % 100 != 0:
        return  29
    else:
        return 28



def max_days_in_month(year,month):

        days = 0
        if month in [1,3,5,7,8,10,12]:
            days = 31
        elif month in [4,6,9,11]:
            days = 30
        elif month in [2]:
            if  is_leapyear(year):
                days = 29
            else:
                days = 28


        return days



def main():


    for year in range(1900,2000):
      for month in range(1,13):
          for days in range(1,max_days_in_month(year,month)):
              if is_magicdate(year ,month, days ):
                  print(f"The Magic date: {year}/{month}/{days}")



    # is_magicdate(1988,4, 22)
    # print(is_magicdate(1988,5,22))
    # print(is_leapyear(1996))
    # print(max_days_in_month(1996,2))



if __name__ == "__main__":
    main()
    