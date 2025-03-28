# Aim:
- To explore the use of Python in the interactive and script modes in Linux.
## Interactive Mode Exercises:
1. Execute the following in interactive mode:
	𝑤𝑖𝑑𝑡ℎ = 17
	ℎ𝑒𝑖𝑔ℎ𝑡 = 12.0
	𝑑𝑒𝑙𝑖𝑚𝑖𝑡𝑒𝑟 = ′𝑎′
	Execute each of the following expressions and write the value of the expression and the type of the values obtained:
	• 𝑤𝑖𝑑𝑡ℎ/2
	• 𝑤𝑖𝑑𝑡ℎ/2.0
	• ℎ𝑒𝑖𝑔ℎ𝑡/3
	• 1 + 2 ∗ 5
	• 𝑑𝑒𝑙𝑖𝑚𝑖𝑡𝑒𝑟 ∗ 5
	![[Screenshot from 2025-02-14 13-07-49.png]]
2. Use the Python interpreter as a calculator to answer the following:
	a. The volume of a sphere with radius 𝑟 is 4/3 𝜋r^3. What is the volume of a sphere with radius 5?
	b. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
	![[Screenshot from 2025-02-14 13-12-57.png]]

## Script Mode Exercises:
1. Given the unit price of a product and the quantity of the product sold, find the total sale,
using Python in script mode
- **Algorithm**:
	- Step 1: Get the unit price and quantity of a product from the user.
	- Step 2: Calculate the total sale by multiplying the unit price with the quantity of the product.
	- Step 3: Display the result:
- **Program**:
```py
def main():
    price, qty = map(float, input("Enter price and quantity: ").split())
    gross = price * qty
    print(f"Total sales: {gross}")

if __name__ == "__main__":
    main()
```
- **Output**:![[Screenshot from 2025-02-14 13-20-30.png]]
2. Write a program (script mode) to get two integers from a user, store them in variables
𝑎 and 𝑏, and evaluate the following expression
$$c = \frac{(a+b)^2 + 10}{a \times b}$$
- **Algorithm**:
	- Step 1: Get the value of a
	- Step 2: Get the value of b
	- Step 3: Evaluate expression with added parentheses to ensure proper order of operations `((a + b) ** 2 + 10)/(a * b)`
- **Program**:
```py
def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(f"The expression c = {(((a + b) ** 2 + 10)/(a * b))=}")

if __name__ == "__main__":
    main()
```
- **Output**:![[Screenshot from 2025-02-14 13-27-34.png]]

# Result:
Thus, the use of python in the interactive mode and the script mode has been explored.
