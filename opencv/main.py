import cv2 as cv
from ultralytics import YOLO

image = cv.imread("./WhatsApp Image 2026-01-29 at 19.22.13.jpeg")
cap = cv.VideoCapture("./😨😱.mp4")
#cap = cv.VideoCapture(0)

model = YOLO("yolov8s.pt")

frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter("./output_prediction.mp4", fourcc=fourcc, fps=fps, frameSize=(frame_width, frame_height))

if not cap.isOpened():
    print("Error Opening File")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model(frame)
    prediction = result[0].plot()
    out.write(prediction)

    #cv.imshow("Predictions from Yolo",prediction)

    if cv.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
out.release()
cv.destroyAllWindows()


"""if not cap.isOpened():
    print("Error Opening File")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv.resize(frame, dsize=(600, 600))
    result = model(resized_frame)
    prediction = result[0].plot()
    cv.imshow("Predictions from Yolo",prediction)
    if cv.waitKey(25) & 0xff == ord("q"):
        break

cap.release()
cv.destroyAllWindows()"""

"""resized_img = cv.resize(image, dsize=(600, 600))
result = model(resized_img)

prediction = result[0].plot()

cv.imwrite("./image_predicted.jpg", prediction)"""

#cv.imshow("image",prediction)
#cv.waitKey(0)
#cv.destroyAllWindows()

"""#cv.imshow("Image",image)
resized_image = cv.resize(image, dsize=(600, 600))
blured_img = cv.GaussianBlur(resized_image, (3, 3), 0)
edge = cv.Canny(blured_img, 100, 100)
rotated_img = cv.rotate(resized_image, cv.ROTATE_180)
change_color = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)

cv.imshow("Image", change_color)
cv.waitKey(0)
cv.destroyAllWindows()"""

"""if not cap.isOpened():
    print("failed to open video")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    resized_frame = cv.resize(frame, dsize=(600, 600))
    gray_frame = cv.cvtColor(resized_frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video", gray_frame)
    if cv.waitKey(25) & 0xff == ord("q"):
        break

cap.release()
cv.destroyAllWindows()"""
