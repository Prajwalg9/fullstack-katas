import cv2

video = cv2.VideoCapture('images/forest_image.png')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output.mp4', fourcc, 25.0, (1920, 1080))

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    output.write(frame)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(10) == ord('s'):
        break

video.release()
output.release()
cv2.destroyAllWindows()
