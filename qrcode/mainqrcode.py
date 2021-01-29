import pyqrcode
site = "www.linkedin.com/in/diontelett"
url = pyqrcode.create(site)
url.png("djlett.png", scale=8)


