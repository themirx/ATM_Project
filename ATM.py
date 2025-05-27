import hashlib
import urllib.request
from random import randint
import os
from dotenv import load_dotenv

load_dotenv() 


card_number = "1234567890123456"
cvv2 = 123
expiry_date = "12/34"
balance = 200000

class ATM:
    def __init__(self, card_number, cvv2, expiry_date, balance):
        self.card_number = card_number
        self.cvv2 = cvv2
        self.expiry_date = expiry_date
        self.balance = balance
        self.phone_number = None

    def get_phone_number(self):
        print("📞 Enter your phone number:")
        phone_number = input("Phone Number: ")
        if len(phone_number) == 11 and phone_number.isdigit():
            self.phone_number = phone_number
            print("✅ Phone number set successfully")
        else:
            print("❌ Invalid phone number format. Please enter an 11-digit number.")
            self.get_phone_number()
        return self.phone_number

    def get_customer_card_input(self):
        print("\n🔒 Enter your card details:")
        card_number1 = input("Card Number: ")
        cvv21 = int(input("CVV2: "))
        expiry_date1 = input("Expiry Date (MM/YY): ")
        return card_number1, cvv21, expiry_date1

    def verify_card(self):
        card_number1, cvv21, expiry_date1 = self.get_customer_card_input()
        if (self.card_number == card_number1 and
            self.cvv2 == cvv21 and
            self.expiry_date == expiry_date1):
            print("Card verified 🧙‍♂️")
            return True
        print("❌ Incorrect card details")
        return False

    def generate_verification_code(self):
        if not self.phone_number:
            self.get_phone_number()
        code = str(randint(10000, 99999))
        self.verification_code = hashlib.sha256(code.encode()).hexdigest()
        self.send_verification_code(code)
        print("🔑 Verification code sent to:", self.phone_number)
        return self.verification_code

    def send_verification_code(self, code):
        api_key = os.getenv("KAVENEGAR_API_KEY")
        api_url = f"https://api.kavenegar.com/v1/{api_key}/verify/lookup.json?receptor={self.phone_number}&token={code}&template=testolgo"
        try:
            urllib.request.urlopen(api_url)
        except Exception as e:
            print("⚠️ Failed to send SMS:", e)

    def verify_verification_code(self):
        user_code = input("Enter verification code: ")
        hashed_input = hashlib.sha256(user_code.encode()).hexdigest()
        if hashed_input == self.verification_code:
            print("✅ Verification successful")
            return True
        else:
            print("❌ Verification failed")
            return False

    def perform_transaction(self):
        if not self.verify_card():
            return
        self.get_phone_number()
        self.generate_verification_code()
        if not self.verify_verification_code():
            return

        print("\n💰 Choose a transaction:")
        print("1. Deposit")
        print("2. Withdraw")
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"✅ Deposit successful! New balance: {self.balance} Toman")
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            if amount > self.balance:
                print("❌ Insufficient balance!")
            else:
                self.balance -= amount
                print(f"✅ Withdrawal successful! New balance: {self.balance} Toman")
        else:
            print("❌ Invalid choice!")


def main():
    atm = ATM(card_number, cvv2, expiry_date, balance)
    while True:
        print("\n🏦 Welcome to the ATM")
        atm.perform_transaction()
        cont = input("Do you want to perform another transaction? (yes/no): ").strip().lower()
        if cont == 'no':
            print("Thank you for using the ATM. Goodbye!")
            break


if __name__ == "__main__":
    main()
