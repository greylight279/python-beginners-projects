import qrcode
from PIL import Image

#making the qrcode genrator function that take the data and imagename
def Qrgenerator(data,imgname):
    qr=qrcode.QRCode(
        version=10,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=4,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img=qr.make_image()
    filepath=(f"C:/Users/ACER/Desktop/python projects/Qr/qrimages/{imgname}.png")

    qr_img.save(filepath)


data=input("Enter the data :")
filename=input("Enter the image name u want to save as :")
Qrgenerator(data,filename)
