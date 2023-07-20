import cv2
#loading cascade file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#capturing video from web cam
videosorce = cv2.VideoCapture(0)
#running while loop
while True:
    _, img = videosorce.read()
    #converting video colour
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #creating a function for detecting faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #running for loop
    for (x, y, w, h) in faces:
        #creating a rectangle
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #displaying results
    cv2.imshow('img', img)
    #Creating a function to close a script
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
videosorce.release()
