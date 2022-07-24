import pyqrcode
import png
import pyqrcode 
# stringof QRCode
qrcode_string="www.ctrlrodz.dev"
# Generate QRCode
url = pyqrcode.create(qrcode_string)
# Save QRCode
url.svg("myqrcode.svg",scale=8)
url.png("myqrcode.png",scale =6)
