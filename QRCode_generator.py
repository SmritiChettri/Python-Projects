''' 
install Segno
$ python -m pip install segno
$ python -m pip install pillow qrcode-artistic

- make_qr() function creates a QR code
- save() method saves QR code as an image which can be viewed and scanned
- scale = value, within save() method adjust the size of QR code
- border = value, within save() method adjusts the blank space i.e quite zone margin around QR code
- light = color-name, within save() method replace white background to chosen color
- dark = color-name, within save() method replace black module to chosen color
- quiet_zone = color-name, within save() method replace the blank margin with chosen color
- data_dark = color-name, within save() method replace the dark data module to chosen color
- data_light = color-name, within save() method replace the data light module to chosen color
ROTATION & ANIMATION
- to_pil() method along with degree of rotation in rotate() create a qr code rotated by chosen degree
'''

import segno
import urllib.request

qrCode = segno.make_qr("Hello,World!")
#BASIC QR Code
qrCode.save("qr_basic.png",
            scale = 9,
            border = 4,
            light = "pink",
            dark = "green",
            quiet_zone = "black",
            data_dark = "red",
            data_light = "lightblue"
 )
 # ROTATED QR code
qr_rotated = qrCode.to_pil(
            scale = 8,
            border = 2,
            light = "pink",
            dark = "green",
            quiet_zone = "black",
            data_dark = "red",
            data_light = "lightblue"
            ).rotate(45, expand = True)
qr_rotated.save("qr_rotate.png")

# ANIMATED QR code
ani_qr = segno.make_qr("Neuvie hydro blast")
neuvie_url = urllib.request.urlopen("https://media1.tenor.com/m/1vkvpSAeXZoAAAAC/neuvillette-360.gif")
ani_qr.to_artistic(
    background = neuvie_url,
    scale = 8,
    target = "qr.gif",
)

