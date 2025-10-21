import cv2

    # Define your GStreamer pipeline string here
gst_pipeline = (
            "v4l2src device=/dev/video0 ! "
            "video/x-bayer, width=1920, height=1080, framerate=30/1, format=rggb ! "
            "bayer2rgb ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! "
            "appsink"
        )

#cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("IMX219 Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()