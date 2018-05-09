import cv2
import pathlib

from os import listdir

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
list = []
namelist = []
currentDirectory = pathlib.Path('./TrainedFaces/')

model = cv2.face.LBPHFaceRecognizer_create()
model.read('./TrainedFaces/DataBase.json')
class Name_confidance:
    person_name = ''
    confidence = 0

def face_detector(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
        return img, roi

cap = cv2.VideoCapture(0)
image = 0
while True:

    ret, frame = cap.read()
    image, face = face_detector(frame)
    cv2.imshow('Face Recognition', image)
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            min = 500
            results = model.predict(face)
            if results[1] < min:
                min = results[1]
                dir = listdir('./faces/')
                for folder in dir:
                    if str(folder).split('.')[1] == str(results[0]):
                        Name_confidance.person_name = str(folder).split('.')[0]
            if min < 500:
                Name_confidance.confidence = int(100 * (1 - (min) / 400))
                display_string = str( Name_confidance.confidence) + '% Confident it is ' + Name_confidance.person_name
                cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 150), 2)

            if  Name_confidance.confidence > 75:
                cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Recognition', image)
            else:
                cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Recognition', image)

        except:
            cv2.putText(image, "No Face Found", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Recognition', image)
            pass
        break
while True:
    cv2.imshow('Face Recognition', image)
    if cv2.waitKey(1) == 13:
        cap.release()
        cv2.destroyAllWindows()
        break