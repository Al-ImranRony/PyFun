# Face detection using opencv

import cv2
import sys

sys.path.append('Users/imran/AppData/Roaming/Python/Python38/site-packages')

image = sys.argv[1]
face_cascade = cv2.CascadeClassifier('face_detector.xml')  # Load the cascade
img = cv2.imread(image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)        # Detect faces
for (x, y, w, h) in faces:                                 # Draw rectangle
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('colorPhoto.jpg', img)
    cv2.waitKey()

# Export the result
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')