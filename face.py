import cv2

def test_camera():
    cap = cv2.VideoCapture(0)  # Try different indices like 1, 2 if this doesn't work

    if not cap.isOpened():
        print("Error: Could not open video device")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow('Camera Test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

test_camera()
