# from currency_converter import CurrencyConverter

# c = CurrencyConverter()

# amt = float(input("Enter amount in USD: "))
# new_amt = c.convert(amt,"USD", "INR")
# print(f"Amount in INR: {new_amt}")


import qrcode

image = qrcode.make("Code with nandan")
image.save("ab_qr.png")
print("QR code generation successfull")

