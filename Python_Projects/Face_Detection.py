#Распознавание лиц на изображении с помощью каскадных классификаторов

Вместо картинки можете использовать свою фотографию.


import cv2

# загрузка каскадного классификатора для распознавания лиц
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# загрузка изображения
img = cv2.imread('face.jpg')

# преобразование в оттенки серого
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# распознавание лиц на изображении
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# отображение прямоугольников вокруг распознанных лиц
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# отображение исходного изображения с прямоугольниками вокруг лиц
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
