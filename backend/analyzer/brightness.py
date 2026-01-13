import cv2
import numpy as np

def calculate_brightness(image: np.ndarray) -> float:
    """
    Calculate average brightness.
    Returns a value between 0 and 255.
    """
    if len(image.shape) == 3:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # V channel represents brightness
        v_channel = hsv[:, :, 2]
        score = np.mean(v_channel)
    else:
        score = np.mean(image)
        
    return float(score)
