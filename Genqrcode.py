import qrcode

# The URL you want to encode
url = "https://github.com/comms-GS-subsystem/TAFITI-user-Interface/blob/main/contributors.md"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("contributors.png")
