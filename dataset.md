## Створення Дата Сету
### Підключення необхідних бібліотек 
```python
import cv2
from os import makedirs
import numpy as np
from os import listdir
from os.path import isfile, join
```
### Завантаження Класифікатора Лиць
```python
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
```
### Введення ім'я, по якому поточний користувач буде записаний в базі даних
```python
name = input("Pls input your name\n")
data_path = './faces/' + name + '/'
makedirs(data_path) #створення директорії з ім'ям користувача
```
### Функція яка повертає сіре вирізане лице з вхідного зображення
```python
def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#повертає сіре зображення
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)#повертає верхню ліву та праву нижню координати лиць
    if faces is (): #якщо на вхідному зображенні не було помічено лиця то повертає None
        return None

    for (x, y, w, h) in faces: #якщо лице було помічено, то повертає вирізане зображення.
        cropped_face = img[y:y + h, x:x + w]
    return cropped_face
```
### Запускаємо відео
```python 
cap = cv2.VideoCapture(0) # Запускаємо відео
count = 0 #Встановлюємо каунтер вже зроблених фото
while True:
    ret, frame = cap.read() #покадрово зчитуємо зображення
    if face_extractor(frame) is not None: #якщо на зчитаному зображенні є лице, то додаємо його до дата сету
        count += 1 
        face = cv2.resize(face_extractor(frame), (200, 200)) #змінюємо розмір зображення
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        file_name_path = data_path + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)#Збереження зображення

        cv2.putText(face, str(count), (50, 50),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2) #показує користувачу скільки вже зроблено зображень
        cv2.imshow('Face Cropper', face) #назва вікна
    else: # Якщо лиця не знайдено, виводить в консоль нижче зазначений текст
        print("Face not found")
        pass
    if cv2.waitKey(1) == 13 or count == 100:  # Якщо буде натиснуто ентер або добавлено 100 зображень лиць, то цикл завершиться.
        break

cap.release()#завершає відео зйомку
cv2.destroyAllWindows()
print("Collecting Samples Complete")
```
### Результат виконання
![відповідь](DataSet.jpg "Приклад відповіді")