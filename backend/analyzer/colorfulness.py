import cv2
import numpy as np

def calculate_colorfulness(image: np.ndarray) -> float:
    """
    Calculate colorfulness using Hasler and Suesstrunk's metric.
    Ref: Hasler, D. and Suesstrunk, S.E., "Measuring colorfulness in natural images," 2003.
    """
    if len(image.shape) < 3:
        return 0.0

    # Convert to float to avoid overflow/underflow and handle negatives
    # OpenCV loads in BGR format
    img_float = image.astype("float")
    B, G, R = cv2.split(img_float)

    # Opponent color spaces
    # rg = R - G
    rg = R - G
    
    # yb = 0.5 * (R + G) - B
    yb = 0.5 * (R + G) - B

    # Compute mean and standard deviation
    std_rg = np.std(rg)
    mean_rg = np.mean(rg)
    
    std_yb = np.std(yb)
    mean_yb = np.mean(yb)

    # Combine
    std_root = np.sqrt(std_rg**2 + std_yb**2)
    mean_root = np.sqrt(mean_rg**2 + mean_yb**2)

    return float(std_root + 0.3 * mean_root)
