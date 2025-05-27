# 🏧 ATM Project

A simple, console-based ATM simulation built with **Python**.  
The code is designed to be **beginner-friendly** and demonstrates key programming concepts including **user input validation**, **authentication**, **verification via phone**, and **basic transactions** (deposit & withdraw).  
While it's not fully OOP-structured, it uses an `ATM` class to encapsulate core logic.

---

## 📌 What This Project Does

- 🔒 Card information input & verification
- 📞 Phone number validation
- 📤 One-time password (OTP) generation & SMS sending via **Kavenegar API**
- ✅ OTP verification using hashed values
- 💰 Balance deposit & withdrawal
- 🔁 Reusable transaction loop with multiple operations

---

## ⚙️ How It Works

1. User is prompted to enter card number, CVV2, and expiry date
2. If the info matches, they're asked for their phone number
3. An OTP (5-digit code) is sent via **Kavenegar API**
4. The user enters the OTP to verify identity
5. Once verified, user chooses to **deposit** or **withdraw**
6. System updates the balance and prints the result

---

## 🔐 Authentication Details

- Static card info is hardcoded for demo:
  - Card Number: `1234567890123456`
  - CVV2: `123`
  - Expiry: `12/34`
- Phone number must be a valid **11-digit number**
- OTP is sent using the `KAVENEGAR_API_KEY` stored in a `.env` file

---

## 🛠️ Installation

```bash
git clone https://github.com/themirx/ATM_project.git
cd ATM_project
pip install python-dotenv
# Make sure you have a .env file with your Kavenegar API key
echo KAVENEGAR_API_KEY=your_api_key > .env
python ATM.py
