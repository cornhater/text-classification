from PIL import Image
import pytesseract
import os

path_npa = (r'C:\Users\Ильяс\Desktop\botay\прога\train_sample\train_sample\npa')
path_tz = (r'C:\Users\Ильяс\Desktop\botay\прога\train_sample\train_sample\tz')
images_npa = os.listdir(path_npa)
images_tz = os.listdir(path_tz)
num = 0
for idx in images_npa:
    image = idx
    img = os.path.join(path_npa, image)
    text = pytesseract.image_to_string(Image.open(img), lang='rus')
    num += 1
    filename = '{name}.txt'.format(name=num)
    file = open(filename, 'w')
    file.write(text)
    file.close

num = 1000
for idx in images_tz:
    image = idx
    img = os.path.join(path_tz, image)
    text = pytesseract.image_to_string(Image.open(img), lang='rus')
    num += 1
    filename = '{name}.txt'.format(name=num)
    file = open(filename, 'w')
    file.write(text)
    file.close