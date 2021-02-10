import cv2 
import imutils
from playsound import playsound


cap = cv2.VideoCapture(0)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 
l = []

while cap.isOpened(): 
    ret, image = cap.read() 
    if ret: 
        image = imutils.resize(image,  
                               width=min(400, image.shape[1])) 
   
        (regions, _) = hog.detectMultiScale(image, 
                                            winStride=(4, 4), 
                                            padding=(4, 4), 
                                            scale=1.05) 
   
            
        for (x, y, w, h) in regions: 
            l.append(cv2.rectangle(image, (x, y), 
                          (x + w, y + h),  
                          (0, 0, 255), 2))
            playsound('Alarm-Fast-A1-www.fesliyanstudios.com.mp3')

            
   
        cv2.imshow("Image", image) 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
    else: 
        break
  
print(l)
cap.release() 
cv2.destroyAllWindows() 