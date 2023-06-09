import pyautogui
import random
import time
import win32api
import win32con
from pynput import mouse

# Disable PyAutoGUI's fail-safe feature
pyautogui.FAILSAFE = False

# Get the monitor resolution
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# Define the center of the screen
centerX = width // 2
centerY = height // 2

# Define the on_click function for the mouse listener
def on_click(x, y, button, pressed):
    if button == mouse.Button.right:
        return False

# Set up the mouse listener
listener = mouse.Listener(on_click=on_click)
listener.start()

# Define the mouse button constant
MOUSE_BUTTON = 'left'

# Wait for 5 seconds before starting mouse movement
time.sleep(5)

# Move the mouse randomly within the monitor resolution
while listener.running:
    try:
        x, y = pyautogui.position()

        # Calculate the new position for the mouse
        newX = x + random.randint(-200, 200)
        newY = y + random.randint(-200, 200)

        # Make sure the new position stays within the monitor resolution
        newX = max(0, min(newX, width))
        newY = max(0, min(newY, height))

        # Move the mouse to the new position
        pyautogui.moveTo(newX, newY, duration=0.2)

        # Add 10% chance of left-clicking at the center of the screen
        if random.random() < 0.3:
            pyautogui.moveTo(centerX, centerY, duration=0.2)
            pyautogui.click(button=MOUSE_BUTTON)


        # Wait for 4 to 6 seconds before starting the next mouse movement
        time.sleep(random.uniform(4, 6))
    except Exception as e:
        print(f"Error: {e}")
