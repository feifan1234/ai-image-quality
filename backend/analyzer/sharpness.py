import cv2
import numpy as np

def calculate_sharpness(image: np.ndarray) -> float:
    """
    Calculate sharpness using the variance of the Laplacian.
    Higher values generally mean sharper images.
    """
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
        
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    score = laplacian.var()
    return float(score)
