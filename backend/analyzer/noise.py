import cv2
import numpy as np

def estimate_noise(image: np.ndarray) -> float:
    """
    Estimate noise using a fast estimation method (Laplacian mask).
    Note: This is a simplified heuristic. Lower is usually better (less noise/texture).
    However, highly textured images might have high values here too.
    """
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    H, W = gray.shape
    
    # Laplacian mask
    M = [[1, -2, 1],
         [-2, 4, -2],
         [1, -2, 1]]
    
    sigma = np.sum(np.sum(np.absolute(cv2.filter2D(gray, -1, np.array(M)))))
    
    # Normalize
    sigma = sigma * np.sqrt(0.5 * np.pi) / (6 * (W-2) * (H-2))
    
    return float(sigma)
