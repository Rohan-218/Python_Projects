import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size =10,
                   border = 5,)
qr.add_data(" https://www.instagram.com/p/Cqis3SHD-4L/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA== ")
qr.make(fit=True)
img = qr.make_image(fill_color = "violet",back_color="lightblue")
img.save("Insta.png")