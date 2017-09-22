import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Reading image from the local directory
image = cv2.imread("shah2.jpg")
# Converting the image from color to gray scale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# Selecting the face
faces = face_cascade.detectMultiScale(gray_image,
scaleFactor=1.05,
minNeighbors =5)

# Creating rectangle shape cascade
for x,y,h,w in faces:
    img = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)

resized_image = cv2.resize(image, (int(image.shape[1]),int(image.shape[0])))

cv2.imshow("Gray",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

