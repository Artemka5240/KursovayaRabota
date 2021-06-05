# KursovayaRabota
Курсовую работу выполнили студенты группы ИДБ-18-11, Баданов Артем Андреевич
Самойлов Степан Сергеевич, ИДБ-18-10
Задание на курсовой проект : создание нейронной сети по разпознаванию "капч"
Задача проекта - научиться работать с языком программирования Python в среде разработки нейронных сетей.

## Цели: ##
- Разделить captcha в соотношении 0.75% и 0.25% для обучения и распознавания соответственно
- Очистить captcha от шумов и если нужно, то повернуть 
- Распознать captcha сначала без обучения с шумом и без него
- Обучить tesseract, распознать captcha c шумом и без него

Ссылка на презентацию проекта - https://cloud.mail.ru/public/5iVY/5Xispt3cB
Ссылка на капчи для обучения - https://cloud.mail.ru/public/2H1t/iLKMafPYE

## Требования: ##
- Установленный tesseract https://github.com/tesseract-ocr/tesseract
- Установленный pipenv https://github.com/pypa/pipenv
- Python >= 3.9

## Установка: ##
```console
git clone https://github.com/Artemka5240/KursovayaRabota.git
cd KursovayaRabota
pipenv install
```

## Обучение Tesseract. ##
- Запускаем программу PyCharm.
- Вызываем функцию imageWithoutGarbage.
- Вызываем функцию createBoxFile.
- Вызываем скрипт trainer.py.

## Распознавание капч: ##
```console
pipenv shell
python app/img_recognition.py "images/{путь к капче}"
```
