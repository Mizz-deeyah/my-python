import sqlite3
from datetime import datetime
import random
import os

# ================= DATABASE =================
conn = sqlite3.connect("bank.db")
cur = conn.cursor()

def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        pin TEXT,
        balance REAL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id TEXT,
        username TEXT,
        type TEXT,
        amount REAL,
        details TEXT,
        time TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id TEXT,
        username TEXT,
        message TEXT,
        time TEXT
    )
    """)

    conn.commit()

init_db()

# ================= UI =================
BANK_NAME = "PYTHON SMART BANK 🏦"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def acc_no(user):
    return str(abs(sum(ord(c) for c in user)))[:10]

def pause():
    input("\nPress Enter...")

def header(user):
    cur.execute("SELECT balance FROM users WHERE username=?", (user,))
    result = cur.fetchone()

    if not result:
        print("Account not found")
        return

    bal = result[0]

    clear()
    print(BANK_NAME)
    print("=" * 40)
    print(f"Name: {user}")
    print(f"Account No: {acc_no(user)}")
    print(f"Balance: ₦{bal}")
    print("=" * 40)

# ================= AUTH =================
def create_account():
    user = input("Username: ")
    pin = input("PIN: ")

    cur.execute("INSERT OR IGNORE INTO users VALUES (?,?,?)", (user, pin, 50000))
    conn.commit()

    print("Account created!")
    return user

def login():
    user = input("Username: ")
    pin = input("PIN: ")

    cur.execute("SELECT * FROM users WHERE username=? AND pin=?", (user, pin))
    if cur.fetchone():
        return user

    print("Invalid login")
    return None

def start_menu():
    while True:
        print("\n1 Login")
        print("2 Create Account")
        print("3 Exit")

        c = input("> ")

        if c == "1":
            u = login()
            if u:
                return u

        elif c == "2":
            u = create_account()
            return u

        elif c == "3":
            exit()

# ================= TRANSACTIONS =================
def tx_id():
    return "TXN" + str(random.randint(100000, 999999))

def add_tx(user, t, amt, d):
    cur.execute("""
        INSERT INTO transactions VALUES (?,?,?,?,?,?)
    """, (tx_id(), user, t, amt, d, str(datetime.now())))
    conn.commit()

# ================= BANKING FUNCTIONS =================
def deposit(user):
    amt = float(input("Amount: "))
    cur.execute("UPDATE users SET balance=balance+? WHERE username=?", (amt, user))
    conn.commit()
    add_tx(user, "Deposit", amt, "Deposit")
    print("Done")
    pause()

def withdraw(user):
    amt = float(input("Amount: "))
    pin = input("PIN: ")

    cur.execute("SELECT pin,balance FROM users WHERE username=?", (user,))
    p, b = cur.fetchone()

    if pin != p:
        print("Wrong PIN")
        return pause()

    if amt > b:
        print("Insufficient balance")
        return pause()

    cur.execute("UPDATE users SET balance=balance-? WHERE username=?", (amt, user))
    conn.commit()
    add_tx(user, "Withdraw", amt, "Withdraw")
    print("Done")
    pause()

def transfer(user):
    bank = input("Bank: ")
    acc = input("Account: ")
    amt = float(input("Amount: "))
    pin = input("PIN: ")

    cur.execute("SELECT pin,balance FROM users WHERE username=?", (user,))
    p, b = cur.fetchone()

    if pin != p:
        print("Wrong PIN")
        return pause()

    total = amt + 50

    if total > b:
        print("Insufficient balance")
        return pause()

    cur.execute("UPDATE users SET balance=balance-? WHERE username=?", (total, user))
    conn.commit()

    add_tx(user, "Transfer", amt, f"{bank}-{acc}")
    print("Transfer successful")
    pause()

def airtime(user):
    amt = float(input("Airtime: "))
    cur.execute("UPDATE users SET balance=balance-? WHERE username=?", (amt, user))
    conn.commit()
    add_tx(user, "Airtime", amt, "Airtime")
    print("Sent")
    pause()

def data(user):
    print("1=300 2=500 3=1000")
    c = input("Plan: ")
    p = {"1":300,"2":500,"3":1000}

    if c not in p:
        return pause()

    cur.execute("UPDATE users SET balance=balance-? WHERE username=?", (p[c], user))
    conn.commit()
    add_tx(user, "Data", p[c], "Data")
    print("Activated")
    pause()

def bills(user):
    amt = float(input("Bill: "))
    cur.execute("UPDATE users SET balance=balance-? WHERE username=?", (amt, user))
    conn.commit()
    add_tx(user, "Bill", amt, "Utility")
    print("Paid")
    pause()

# ================= AI =================
def ai(user):
    q = input("Ask AI: ").lower()

    if "balance" in q:
        cur.execute("SELECT balance FROM users WHERE username=?", (user,))
        return f"₦{cur.fetchone()[0]}"

    return "Support available."

# ================= CUSTOMER CARE =================
def care(user):
    while True:
        clear()
        print("💬 CUSTOMER CARE CENTER")
        print("1. Lodge Complaint")
        print("2. Talk to Customer Rep")
        print("3. Exit")

        c = input("> ")

        if c == "1":
            lodge_complaint(user)

        elif c == "2":
            customer_rep()

        elif c == "3":
            break

def lodge_complaint(user):
    clear()
    msg = input("Complaint: ")
    cid = "CMP" + str(random.randint(1000, 9999))

    cur.execute("INSERT INTO complaints VALUES (?,?,?,?)",
                (cid, user, msg, str(datetime.now())))
    conn.commit()

    print("Ticket ID:", cid)
    pause()

def customer_rep():
    clear()
    print("👩‍💻 CUSTOMER REP CHAT")
    print("Type 'exit' to leave\n")

    while True:
        m = input("You: ").strip().lower()

        if m == "":
            print("Rep: Please type a message or 'exit'")
            continue

        if m == "exit":
            print("Rep: Chat ended. Have a nice day!")
            pause()
            break

        if "transfer" in m:
            print("Rep: Check account number, PIN, or balance.")

        elif "complaint" in m:
            print("Rep: Use Customer Care menu to lodge complaints.")

        elif "failed" in m:
            print("Rep: We are reviewing your transaction.")

        elif "hello" in m:
            print("Rep: Hello 👋 how can I help you?")

        else:
            print("Rep: Message received. We will respond shortly.")

# ================= MAIN =================
user = start_menu()
header(user)

while True:
    print("""
1 Deposit
2 Withdraw
3 Transfer
4 Airtime
5 Data
6 Bills
7 AI Assistant
8 Customer Care
9 Logout
""")

    o = input("> ")

    if o == "1":
        deposit(user)
    elif o == "2":
        withdraw(user)
    elif o == "3":
        transfer(user)
    elif o == "4":
        airtime(user)
    elif o == "5":
        data(user)
    elif o == "6":
        bills(user)
    elif o == "7":
        print(ai(user))
        pause()
    elif o == "8":
        care(user)
    elif o == "9":
        user = start_menu()
        header(user)