import cv2
from os import makedirs
import numpy as np
from os import listdir
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
class DataPath:
    data_path = ""
def create_directory(directory_name):
    DataPath.data_path = './faces/' + directory_name + '.'  + str(len(listdir('./faces/')))  + '/'
    makedirs(DataPath.data_path)
def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return None
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]
    return cropped_face
def start_creating_data_set(quantity):
    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = DataPath.data_path + str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)
        else:
            print("Face not found")
            pass
        if cv2.waitKey(1) == 13 or count == quantity:  # 13 is the Enter Key
            break

    cap.release()
    cv2.destroyAllWindows()

def trainModel():
    dirs = listdir('./faces/')
    Training_Data, Labels = [], []
    for dir_name in dirs:
        subfolder_list = listdir('./faces/' + dir_name + '/')
        for images in subfolder_list:
            faces = cv2.imread('./faces/'  + str(dir_name) + '/' + str(images))
            gray = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)
            Training_Data.append(gray)
            Labels.append(int(dir_name.split(".")[1]))
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(Training_Data, np.asarray(Labels))
    model.save('./TrainedFaces/DataBase.json')

trainModel()