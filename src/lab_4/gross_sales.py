"""
    Given the unit price of a product and the quantity of the product sold, find the total sale,
    using Python in script mode.
"""

def main():
    price, qty = map(float, input("Enter price and quantity: ").split())
    gross = price * qty
    print(f"Total sales: {gross}")

if __name__ == "__main__":
    main()