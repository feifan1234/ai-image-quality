import cv2
import numpy as np

def load_image_from_bytes(image_bytes: bytes) -> np.ndarray:
    """
    Load an image from bytes (e.g., from an upload) into an OpenCV numpy array.
    """
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Could not decode image")
    return img
