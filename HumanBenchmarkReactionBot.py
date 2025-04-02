import mss
import numpy as np
from pynput.mouse import Controller, Button
import time

# Coordinates where the game expects a click
GAME_POS = (960, 540)  # Adjust based on your screen resolution

# RGB Color of the green screen
GREEN_COLOR = (106, 219, 75)  # Approximate color

mouse = Controller()

def get_pixel_color(x, y):
    """Capture a small area around (x, y) and return the pixel color."""
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        return tuple(img[0, 0][:3])  # Extract RGB color

def wait_for_green():
    """Wait for the green screen to appear, then click instantly."""
    print("Waiting for green screen...")
    
    while True:
        detected_color = get_pixel_color(*GAME_POS)

        if detected_color == GREEN_COLOR:
            print("Green detected! Clicking now...")
            mouse.position = GAME_POS
            mouse.click(Button.left, 1)
            break  # Stop checking once clicked

        time.sleep(0.001)  # Check every millisecond for better reaction time

    time.sleep(1)  # Pause before restarting
    print("Restarting test... Click again to begin.")

while True:
    wait_for_green()
    time.sleep(1)  # Give time to restart the game manually
