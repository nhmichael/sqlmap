import requests
from PIL import Image
import pytesseract
def gencapchacode(url,length=4):
	valcode = requests.get(url)
	f = open('valcode.png', 'wb')
	f.write(valcode.content)
	f.close()
	image=Image.open('valcode.png')
	img_gray=image.convert("L")
	code=pytesseract.image_to_string(img_gray, lang='eng', config='--psm 8')
	return code[0:length]

if __name__ == "__main__":
    gencapchacode()
	