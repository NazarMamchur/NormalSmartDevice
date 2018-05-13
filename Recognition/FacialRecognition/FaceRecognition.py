import cv2
from os import listdir

from server.info.settings import FACIAL_RECOGNITION_ROOT
path = FACIAL_RECOGNITION_ROOT

face_classifier = cv2.CascadeClassifier(path + '/haarcascade_frontalface_default.xml')
model = cv2.face.LBPHFaceRecognizer_create()
model.read(path + '/TrainedFaces/DataBase.json')


class Name_confidance:
        person_name = ''
        confidence = 0


def face_detector(img):
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(img, 1.3, 5)
        if faces is ():
            return img, []

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi = img[y:y + h, x:x + w]
            roi = cv2.resize(roi, (200, 200))
            return img, roi


def face_recognizer(img_to_recognize):
    frame = cv2.imread(img_to_recognize)
    image, face = face_detector(frame)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        min = 500
        results = model.predict(face)
        if results[1] < min:
            min = results[1]
            dir = listdir(path + '/faces/')
            for folder in dir:
                if str(folder).split('.')[1] == str(results[0]):
                    Name_confidance.person_name = str(folder).split('.')[0]
        if min < 500:
            Name_confidance.confidence = int(100 * (1 - (min) / 400))

        if Name_confidance.confidence > 75:
            return Name_confidance.person_name + " allowed"
        else:
            return "Not allowed"

    except:
        return "No face found"
        pass
