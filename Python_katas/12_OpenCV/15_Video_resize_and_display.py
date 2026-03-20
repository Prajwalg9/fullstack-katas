import cv2

video = cv2.VideoCapture('images/nature.mp4')

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 720))
    cv2.imshow('Output', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
