import re
import os
import sys
import pytesseract
from createBoxFile import imageWithoutGarbage


ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
TRAINED_ROOT = os.path.join(ROOT, 'traineddata/')


def captchaDirRecognition(path):
    # каталог с капчами, которые нужно распознать
    catalogWithCaptcha = os.listdir(path)

    count = 0
    for captcha in catalogWithCaptcha:
        if captchaRecognition(captcha):
            count += 1

    # число правиьлно распознаных капч
    return count


def captchaRecognition(captcha):

    captchaName = re.findall(r'.*?ttf_(.*?)_', captcha)
    captchaName = re.sub(r'.png', '', captchaName[0])

    result = pytesseract.image_to_string(imageWithoutGarbage(ROOT + str(captcha)), lang='arial+campanella+montesuma+times+ryuk+minecraft+eng', config='--tessdata-dir ' + TRAINED_ROOT)
    result = re.sub(r'\n.*', '', result)
    print(captchaName)
    print(result)
    if captchaName == result:
        return True
    return False


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) else None
    if not path:
        print('Вы не указали путь к изображению')
        sys.exit()
    print(captchaRecognition(path))
