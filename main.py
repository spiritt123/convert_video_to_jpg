import cv2
import numpy as np
print(cv2.__version__)
name = input()
vidcap = cv2.VideoCapture(name)
success,image = vidcap.read()
count = 0
success = True
output = []
buffer1 = []
while success:
  output.append(image[52])
  output.append(image[51])
  output.append(image[50])
  success,image = vidcap.read()
  count += 1
  if count == 50:
      buffer1 = image
output = output[::-1]
for i in range(200, 360):
    output.append(buffer1[i])
cv2.imwrite("./"+name[0:-4]+".jpg", np.asarray(output))
