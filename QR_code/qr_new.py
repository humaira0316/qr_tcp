import qrcode
from PIL import Image


qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4)
website_link = input("Enter the link to generate QR :")
qr.add_data(website_link)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="black")
img.save("qrofgeekscn.png")
