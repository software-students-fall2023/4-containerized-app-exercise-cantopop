import cv2

def capture_image():
    """
    Captures a single image from the default camera and returns the image.
    Make sure to handle the release of the camera resource in a finally block.
    """

    # Initialize the camera
    cap = cv2.VideoCapture(0)  # '0' is typically the default camera

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    try:
        ret, frame = cap.read()
        if not ret:
            raise IOError("Cannot capture image from camera")
        
        return frame

    finally:
        cap.release()

def save_image(image, filename="captured_image.jpg"):
    """
    Saves the captured image to the specified file.
    """
    cv2.imwrite(filename, image)
