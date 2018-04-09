import cv2
import pathlib

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
list = []
namelist = []
currentDirectory = pathlib.Path('./TrainedFaces/')
for currentFile in currentDirectory.iterdir():
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read(str(currentFile))
    namelist.append(str(currentFile).split('\\')[1])
    list.append(model)
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

            for i in range(0,len(list)):
                results = list[i].predict(face)
                print(i)
                if(results[1] < min):
                    min = results[1]
                    index = i

            if min < 500:
                confidence = int(100 * (1 - (min) / 400))
                display_string = str(confidence) + '% Confident it is ' + namelist[index].split('.')[0]
            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 150), 2)

            if confidence > 75:
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