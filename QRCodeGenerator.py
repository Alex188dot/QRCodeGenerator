import segno

qr_code = segno.make("https://github.com/Alex188dot")
qr_code.save("Alessio's_Github.png", dark="#ffb10b", light="#f7ff0b", scale=10)
print('QR created successfully!')
