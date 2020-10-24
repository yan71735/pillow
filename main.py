from PIL import Image, ImageDraw, ImageFont
import requests
import sys

url = input('Paste URL of ur image: ')

try:
    response = requests.get(url, stream=True).raw
    print(response)
except requests.exceptions.RequestException:
    print('Подключение не удалось!')
    sys.exit(1)

try:
    img = Image.open(response)
    print('Image opened!')
except IOError:
    print('Unable to open!')
    sys.exit(1)

img.save('saved_from_inet.jpg') # сохраняем изображение из интернета

idraw = ImageDraw.Draw(img)  # на чем рисовать
text = 'YANSHABANAU'  # что писать

font = ImageFont.truetype(r'BillionDreams_PERSONAL.ttf', size=128)
idraw.text((500, 500), text, font=font)

img.save('water.jpg')
