import cv2 as cv
from ultralytics import YOLO

model = YOLO("yolov8s.pt")

cap = cv.VideoCapture(0)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS))

fourcc = cv.VideoWriter_fourcc(*"mp4v")

out = cv.VideoWriter("./Predicted_OutputVideo.mp4", fourcc, fps, frameSize=(width, height))

if not cap.isOpened():
    print("Error oppening File")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #resized_img = cv.resize(frame, dsize=(600, 600))
    pred = model(frame)
    result = pred[0].plot()
    out.write(result)
    cv.imshow("Video", result)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv.destroyAllWindows()

""" cap = cv.VideoCapture("./me.mp4")
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS))

fourcc = cv.VideoWriter_fourcc(*"mp4v")

out = cv.VideoWriter("./PredictedOutputVideo.mp4", fourcc, fps, frameSize=(width, height))

if not cap.isOpened():
    print("Error oppening File")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #resized_img = cv.resize(frame, dsize=(600, 600))
    pred = model(frame)
    result = pred[0].plot()
    out.write(result)
    #cv.imshow("Video", result)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv.destroyAllWindows() """

""" 
#image = cv.imread("./download.jpg")
image = cv.imread("./alotgoingon.jpg")
resized_img = cv.resize(image, dsize=(600, 600))
edges = cv.Canny(resized_img, 100, 150)
color = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)


pred = model(resized_img)
result = pred[0].plot()

#cv.imwrite("./predicted_img.jpg", result)
cv.imwrite("./predicted_img2.jpg", result)


cv.imshow("Yolo Predicted Image", result)
cv.waitKey(0)
cv.destroyAllWindows() """