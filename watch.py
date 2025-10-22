import time
import cv2
import sqlite3
conn = sqlite3.connect("movimiento.db")

conn.execute("create table if not exists movimiento(tiempo TIMESTAMP DEFAULT CURRENT_TIMESTAMP, x integer, y integer);")
cap = cv2.VideoCapture("tcp://localhost:1234") #adaptar para pi-cam
#cv2.startWindowThread()
#cv2.namedWindow('Frame_final')
#ret, frame = cap.read()
#cv2.imshow('Frame_final', frame)
#cv2.waitKey(1)

backSub = cv2.createBackgroundSubtractorMOG2()
i=0;
if not cap.isOpened():
    print("Error opening video file")
while cap.isOpened():
    # Capture frame-by-frame
      time.sleep(.1)
      ret, frame = cap.read(cv2.IMREAD_REDUCED_GRAYSCALE_4)
      cv2.waitKey(1)
      if ret:
        # Apply background subtraction
        if i==0:
            fg_mask = backSub.apply(frame)
        # Find contours
#        contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours)
        frame_ct = cv2.drawContours(frame, contours, -1, (100, 0, 0), 2)
        # Display the resulting frame
        cv2.imshow('Frame_final', frame_ct)
        # apply global threshold to remove shadows
#        retval, mask_thresh = cv2.threshold(fg_mask, 500, 255, cv2.THRESH_BINARY)
        retval, mask_thresh = cv2.threshold(fg_mask, 500, 255, cv2.THRESH_TOZERO_INV)
        # set the kernal
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
        # Apply erosion
        mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)
        min_contour_area = 1500  # Define your minimum area threshold
        large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
        frame_out = frame.copy()
        for cnt in large_contours:
            x, y, w, h = cv2.boundingRect(cnt)
            conn.execute("insert into movimiento(x,y) values(?,?)",(x+w/2,y+h/2))
            frame_out = cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 200, 0), 3)

        # Display the resulting frame
        cv2.imshow('Frame_final', frame_out)
        if int(time.time()) % 20 == 0:
            conn.commit()
        cv2.waitKey(1)
        i=i+1
        if i>1:
            i=0