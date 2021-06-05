# KursovayaRabota
Курсовую работу выполнили студенты группы ИДБ-18-11, Баданов Артем Андреевич
Самойлов Степан Сергеевич, ИДБ-18-10
Задание на курсовой проект : создание нейронной сети по разпознаванию "капч"
Задача проекта - научиться работать с языком программирования Python в среде разработки нейронных сетей.
Цели проекта : 
1.	Разделить captcha в соотношении 0.75% и 0.25% для обучения и распознавания соответственно
2.	Очистить captcha от шумов и если нужно, то повернуть 
3.	Распознать captcha сначала без обучения с шумом и без него
4.	Обучить tesseract, распознать captcha c шумом и без него


Ссылка на tesseract - https://github.com/tesseract-ocr/tesseract
Ссылка на шрифты - https://cloud.mail.ru/public/csiz/pbfDhj1xg
Ссылка на презентацию проекта - https://cloud.mail.ru/public/5iVY/5Xispt3cB

Инструкция по запуску/установке : 
1.	Проверяем наличие на компьютере следующих библиотек: tesseract, PIL, operator, math, re, os, subprocess, numpy.
2.	Обучение Tesseract.
2.1.	Запускаем программу PyCharm.
2.2.	Вызываем функцию imageWithoutGarbage.
2.3.	Вызываем функцию createBoxFile.
2.4.	Вызываем скрипт trainer.py.
2.5.	перенести созданный файл *.traineddata в корневую папку tessdata: $cp /path/to/data/*.traineddata $TESSDATA_PREFIX/tessdata
3.	Распознавание капч.
3.1.	Вызываем функцию captchaRecognition.

