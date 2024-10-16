import cv2
import numpy as np

def getPositionAutoConf(image_path, template_path, debug=False):
    """Simplified version of getPositionAutoConf that works without Robot Framework."""
    big_img = cv2.imread(image_path)
    temp_img = cv2.imread(template_path)
    
    if big_img is None or temp_img is None:
        print("Error loading images")
        return []

    result = cv2.matchTemplate(big_img, temp_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    threshold = max_val if max_val > 0.8 else 0.8
    locations = np.where(result >= threshold)
    
    found_locations = []
    for pt in zip(*locations[::-1]):  # Switch columns and rows
        x = pt[0] + temp_img.shape[1] // 2
        y = pt[1] + temp_img.shape[0] // 2
        found_locations.append((x, y))
        
        if debug:
            cv2.rectangle(big_img, pt, (pt[0] + temp_img.shape[1], pt[1] + temp_img.shape[0]), (0, 0, 255), 2)
    
    if debug:
        cv2.imwrite("debug_output.png", big_img)
        print(f"Found {len(found_locations)} matches")
    
    return found_locations