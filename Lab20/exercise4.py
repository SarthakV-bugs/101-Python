# Write a function calculate_total_price (no_of_items, unit_price, tax_rate) with an
# inner_function calculate_tax(amount, tax_rate) defined inside it.
# The outer function should call calculate_tax with the total amount for n items and the
# tax_rate passed to it. It should then add the tax to the total amount and return gross
# amount.
# Call the outer function calculate_total_price with different sets of arguments
from typing_extensions import no_type_check


def calculate_total_price (no_of_items, unit_price, tax_rate):
    def calculate_tax(amount, tax_rate):
        tax_amount = amount * tax_rate

        return tax_amount
    amount = no_of_items*unit_price
    gross_amount = amount+calculate_tax(amount,tax_rate)
    return gross_amount

def main():
    no_of_items=int(input("Enter the number:"))
    unit_price = int(input("Enter the unit price: "))
    tax_rate = float(input("Enter the tax rate: "))
    result= calculate_total_price(no_of_items,unit_price, tax_rate)
    print(result)

if __name__ == "__main__":
        main()
