import sqlite3
import getpass

def create_table():
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            pin TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0
        )
    """)
    conn.commit()
    conn.close()

def register():
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    name = input("Enter your name: ")
    pin = getpass.getpass("Enter a 4-digit PIN: ")
    cursor.execute("INSERT INTO users (name, pin, balance) VALUES (?, ?, ?)", (name, pin, 0.0))
    conn.commit()
    conn.close()
    print("Account created successfully")

def login():
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    name = input("Enter your name: ")
    pin = getpass.getpass("Enter your PIN: ")
    cursor.execute("SELECT * FROM users WHERE name=? AND pin=?", (name, pin))
    user = cursor.fetchone()
    conn.close()
    if user:
        atm_menu(user[0])
    else:
        print("Invalid credentials")

def atm_menu(user_id):
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_balance(user_id)
        elif choice == "2":
            deposit(user_id)
        elif choice == "3":
            withdraw(user_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def check_balance(user_id):
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    balance = cursor.fetchone()[0]
    conn.close()
    print(f"Your balance is: {balance}")

def deposit(user_id):
    amount = float(input("Enter amount to deposit: "))
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance + ? WHERE id=?", (amount, user_id))
    conn.commit()
    conn.close()
    print("Deposit successful")

def withdraw(user_id):
    amount = float(input("Enter amount to withdraw: "))
    conn = sqlite3.connect("atm.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    balance = cursor.fetchone()[0]
    if balance >= amount:
        cursor.execute("UPDATE users SET balance = balance - ? WHERE id=?", (amount, user_id))
        conn.commit()
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
    conn.close()

def main():
    create_table()
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

