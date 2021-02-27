import pickle
from PIL import Image
import pytesseract

texts = []
print('Enter path to the image to show its style; Enter "stop" to give the result')
while True:
    path = input()
    if (path == 'stop'):
        break
    img = r'{image}'.format(image=path)
    text = pytesseract.image_to_string(Image.open(img), lang='rus')
    texts.append(text)
with open('my_classifier.pkl', 'rb') as pickle_file:
    clf = pickle.load(pickle_file)
print(clf.predict(texts))