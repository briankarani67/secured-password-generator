import qrcode

data = input("Enter link or text for qrcode: ")

Generate = qrcode.make(data)
Generate.save("qr_code.png")

print("Qr code generated successfully")