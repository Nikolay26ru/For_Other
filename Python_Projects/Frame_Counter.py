# код, который будет выводить на видео информацию о количестве кадров, обрабатываемых в секунду
import cv2
import time

cap = cv2.VideoCapture(0)

prev_time = 0

while True:
    ret, frame = cap.read()

    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
