"""Module for capturing images using a camera."""

import cv2

def capture_image():
    """
    Captures an image from the default camera.
    """
    cap = cv2.VideoCapture(0)  # pylint: disable=no-member
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
    cv2.imwrite(filename, image)  # pylint: disable=no-member
