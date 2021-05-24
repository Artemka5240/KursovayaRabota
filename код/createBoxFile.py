from PIL import Image
from operator import itemgetter
from math import *
import re
import os

# на вход функция получает выборку капч для обучения и путь куда будем складывать созданные box-файлы
def createBoxAndPicture(samplingPath, pathForBoxFile):
    # получаем все капчи из каталога samplingPath
    catalogWithCaptcha = os.listdir(samplingPath)

    # число капч на обучение
    numberOfTestCaptcha = round(0.75 * len(catalogWithCaptcha))

    for i in range(0, numberOfTestCaptcha):

        captcha = catalogWithCaptcha[i]
        captchaName = re.findall(r'.*?ttf_(.*?)_', captcha)

        img = imageWithoutGarbage(str(samplingPath) + '/' + str(captcha))

        box = createBoxFile(captcha, img)

        if box != 0:
            img.save(pathForBoxFile + str(captchaName[0]) + '.png')
            file = open(pathForBoxFile + str(captchaName[0]) + '.box', 'w')
            file.write(box)


# функция для очистки captcha
# на вход функция получает расположение captcha
def imageWithoutGarbage(path):
    # открывем капчу с шумом
    image = Image.open(path)

    # угол поворота
    angled = re.findall(r'_(\-?\d*).gif', path)

    if int(angled[0]) > 0:
        image = image.rotate(- int(angled[0]))

    if int(angled[0]) < 0:
        image = image.rotate(-int(angled[0]))

    # Получаем гистограмму изображения в виде списка
    his = image.histogram()

    values = {}

    # Цвета, которые используются в капче
    arrColor = []

    # Присваиваем цвету, количесвто пикселей этого цвета
    for i in range(256):
        values[i] = his[i]

    # Заполняем массив цветами, которые чаще всего встречаются в капче
    for color, countPixel in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
        arrColor.append(color)

    # создаём новое изображение с параметрами:
    # "P": режим изображения P - 8 бит, цветное (256 цветов)
    # im.size: размер изображения
    # 255: цвет фона белый
    im2 = Image.new("P", image.size, 255)

    width = image.size[0]  # определяем ширину
    height = image.size[1]  # определяем высоту

    # Получаем каждый пиксель капчи и смотрим походит ли он нам
    for x in range(width):
        for y in range(height):

            # получаем пиксель
            pix = image.getpixel((x, y))

            # если цвет подходит, то изменяем цвет пикселя в новом изображении
            if pix == arrColor[1]:  # these are the numbers to get
                # изменяем цвет пикселя в данной позиции
                im2.putpixel((x, y), 0)

    return im2


# функция для создания box файла на основе очищенной captcha
# на вход функция получает очищенную captcha
def createBoxFile(path, img):
    reg = re.findall(r'.*?.ttf_(.*?)_([\d,]+)_([\d,]+)_([\d,]+)_([\-?\d,]+).gif', path)
    leftMargin = 1

    # массив для определения расстояния до верхней и нижней границы массива
    minAndMaxPix = []

    arrBox = []
    width = img.size[0]  # определяем ширину
    height = img.size[1]  # определяем высоту

    # определяем начало и конец каждой буквы в пикселях
    for pixelWide in range(1, width - 1):

        # количество белых пикселей
        countWhite = 0

        for pixelHigh in range(1, height - 1):

            # если пиксель белого цвета  идут два раза подряд значит это отступ между символами
            if img.getpixel((pixelWide, pixelHigh)) == 255 and img.getpixel(
                    (pixelWide + 1, pixelHigh)) == 255 and leftMargin == 0:
                countWhite += 1

            # расстояние до левой границы символа
            if (leftMargin == 1) and (img.getpixel((pixelWide + 1, pixelHigh)) == 0):
                leftMargin = 0

                arrBox.append(pixelWide)

            if (leftMargin == 0) and (img.getpixel((pixelWide, pixelHigh)) == 0):
                minAndMaxPix.append(pixelHigh)

            # если до этого была граница символа слева и было 2 белых пикселя подряд,значит была граница справа
            if countWhite == img.size[1] - 2 and leftMargin == 0:
                leftMargin = 1

                # нижняя граница
                arrBox.append(img.size[1] - max(minAndMaxPix) - 2)

                # до правой границы
                arrBox.append(pixelWide + 1)

                # до верхней границы
                arrBox.append(img.size[1] - min(minAndMaxPix) + 1)

                minAndMaxPix = []

    count = 0
    boxFile = ''
    if len(arrBox) != 4 * int(len(list(reg[0][0]))):
        return 0

    for character in list(reg[0][0]):
        boxFile += str(character)

        for i in range(1, 5):
            boxFile += ' ' + str(arrBox[count])
            count += 1
        boxFile += ' 0\n'

    return boxFile

createBoxAndPicture('./captcha/ryuk', './captcha/ryukTraining/')