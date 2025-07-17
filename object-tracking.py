import cv2

# Load video
cap = cv2.VideoCapture('people_walking.mp4')  # replace with your video filename

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Error reading video")
    cap.release()
    exit()

# Select ROI (Region of Interest)
bbox = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Object to Track")

# Create tracker (you can change CSRT to KCF, MIL, etc.)
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Update tracker
    success, bbox = tracker.update(frame)

    if success:
        # Draw bounding box
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost", (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 0, 255), 2)

    cv2.imshow("Object Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
