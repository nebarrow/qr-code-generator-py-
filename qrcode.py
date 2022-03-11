import qrcode

base = "your link" # url
filename = "qrcode.png" # file name
image = qrcode.make(base) # qr-code generation
image.save(filename) # save image if file