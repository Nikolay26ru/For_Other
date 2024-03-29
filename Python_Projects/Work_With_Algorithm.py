#Алгоритм, реализующий перемещение области интереса  по передаваемому по веб-камере видео, так чтобы в области интереса пиксели были цветные, а остальное было черно-белым.

import cv2
import numpy as np

# открытие видеофайла
cap = cv2.VideoCapture('test.mp4')

# начальные координаты и размеры области интереса
x = 100
y = 100
width = 200
height = 200

# флаги для определения направления движения области интереса
move_right = True
move_down = True

while(cap.isOpened()):
    # чтение кадров видео
    ret, frame = cap.read()

    # проверка наличия кадра
    if ret == True:
        # создание маски для области интереса
        mask = cv2.rectangle(
            img=np.zeros_like(frame),
            pt1=(x, y),
            pt2=(x + width, y + height),
            color=(1, 1, 1),
            thickness=-1
        )

        # применение маски к кадру
        masked_frame = frame * mask

        # преобразование кадра в черно-белый
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

        # объединение цветной и черно-белой частей кадра
        final_frame = masked_frame + gray_frame

        # отображение кадра на экране
        cv2.imshow('frame', final_frame)

        # движение области интереса
        if move_right:
            x += 5
        else:
            x -= 5

        if move_down:
            y += 5
        else:
            y -= 5

        # изменение направления движения при достижении границ кадра
        if x + width >= frame.shape[1]:
            move_right = False
        elif x <= 0:
            move_right = True

        if y + height >= frame.shape[0]:
            move_down = False
        elif y <= 0:
            move_down = True

        # ожидание 25 мс
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# освобождение ресурсов и закрытие окна
cap.release()
cv2.destroyAllWindows()
