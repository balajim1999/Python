import pyqrcode
url = 'http://www.youtube.com/c/ASingleMan1'
k=pyqrcode.create(url)
k.svg('My YouTube Channel',scale=10)
