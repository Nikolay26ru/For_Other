#Определение реальной скорости двидущегося объекта
# В качестве примера используется открытая камера в в Пскове
import cv2
import numpy as np

real_distance_meters = 27
distance_pixels = 580

scale_ratio = real_distance_meters / distance_pixels  # пиксели на метр
print(scale_ratio)
cap = cv2.VideoCapture("https://citycams.pskovline.ru:8443/cam7/mpegts")

# Задаем параметры для optical flow
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

_, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
frame_counter = 0
fps = cap.get(cv2.CAP_PROP_FPS)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    p1, status, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    if p1 is not None:
        good_new = p1[status == 1]
        good_old = p0[status == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()

            speed = np.sqrt((a - c)**2 + (b - d)**2)
            if speed > 5:  # Пороговое значение скорости
                frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)
                speed_meters_frame = speed * scale_ratio  # скорость в метрах на кадр
                speed_meters_sec = speed_meters_frame * fps  # скорость в метрах в секунду
                speed_kmh = speed_meters_sec * 3.6  # скорость в километрах в час

                speed_text = f"Speed: {speed_kmh:.2f} in km/h"
                frame = cv2.putText(frame, speed_text, (int(a), int(b) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4,
                                    (255, 255, 255), 1)

    cv2.imshow("Action Recognition", frame)
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
    frame_counter += 1
    if frame_counter % 10 == 0:
        p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
cap.release()
cv2.destroyAllWindows()
