import cv2
import numpy as np

def calculate_contrast(image: np.ndarray) -> float:
    """
    Calculate contrast using the standard deviation of pixel intensities (RMS Contrast).
    """
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
        
    score = gray.std()
    return float(score)
