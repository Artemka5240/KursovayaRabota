import subprocess
import re
import os

# Функция для распознавания капч
# на вход подаётся путь, где находится выборка, которую нужно распознать
def captchaRecognition(path):

    # каталог с капчами, которые нужно распознать
    catalogWithCaptcha = os.listdir(path)

    count = 0
    for i in range(0, len(catalogWithCaptcha)):
        captcha = catalogWithCaptcha[i]
        captchaName = re.sub(r'.png', '', captcha)
        subprocess.call(['tesseract', str(path)+'/'+str(captcha), 'output', '-l', 'Ryuk+eng'])
        file = open('output.txt', "r")
        print(captcha)
        try:
            fileWithCaptcha = file.read()
        # исключение связанное с декодированием unicode
        except UnicodeDecodeError:
            count += 0
        fileWithCaptcha = re.sub(r'\n.*', '', fileWithCaptcha)
        if captchaName == fileWithCaptcha:
            count += 1

    # число правиьлно распознаных капч
    print(count)
    return count

captchaRecognition("./ryuk на распознавание с мусором и с поворотом")