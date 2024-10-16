import cv2
import numpy as np
import pyautogui
import os
from function import getPositionAutoConf

def capture_screen():
    """Capture the entire screen and return as an OpenCV image."""
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def click_on_match(match):
    """Move the mouse to the match coordinates and click."""
    pyautogui.moveTo(match[0], match[1], duration=0.5)
    pyautogui.click()


def main():
    # Capture the entire screen
    screen = capture_screen()
    
    # Save the captured screen as an image file
    screen_filename = "captured_screen.png"
    cv2.imwrite(screen_filename, screen)
    
    # Path to your template image
    template_path = "./SelectData.png"  # Replace with your template image path
    
    # Use the simplified getPositionAutoConf function
    matches = getPositionAutoConf("captured_screen.png", template_path, debug=True)
    
    if not matches:
        print("No matches found on the screen.")
        return
    
    print(f"Found {len(matches)} matches.")
    
    # Click on the first match
    first_match = matches[0]
    click_on_match(first_match)
    
    print(f"Clicked at coordinates: {first_match}")

    #remove file
    os.remove(screen_filename)

if __name__ == "__main__":
    main()