import cv2
import time

print("Attempting to open webcam...")
cap = cv2.VideoCapture(0) # Try to open the default camera

if not cap.isOpened():
    print("Error: Could not open webcam. Please check if it's connected and drivers are installed.")
    exit() # Exit if camera can't be opened

print("Webcam opened successfully. Showing live feed. Press 'q' to quit or waits 10 seconds.")

start_time = time.time()
while(True):
    ret, frame = cap.read() # Read a frame

    if not ret:
        print("Error: Could not read frame.")
        break # Exit loop if frame can't be read

    cv2.imshow('Webcam Test', frame) # Display the frame

    # Break the loop if 'q' is pressed or after 10 seconds
    if cv2.waitKey(1) & 0xFF == ord('q') or (time.time() - start_time) > 10:
        break

cap.release() # Release the camera
cv2.destroyAllWindows() # Close all OpenCV windows
print("Webcam test finished.")