import pyautogui
import time
import random

# Ask the user for the duration to keep the computer awake (in hours)
duration_hours = float(input("Enter the duration to keep the computer awake in hours (e.g., 1.5 for 1 hour 30 mins): "))
duration_seconds = int(duration_hours * 3600)  # Convert to seconds

end_time = time.time() + duration_seconds

while time.time() < end_time:
    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Generate a random point on the screen
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Generate a random duration for the movement (between 0.1 and 0.6 seconds)
    duration = random.uniform(0.1, 0.6)

    pyautogui.moveTo(x, y, duration=duration)  # Move the mouse to the random point at a random speed

    # Randomly decide whether to perform a scroll (10% chance)
    if random.randint(0, 9) == 0:
        pyautogui.scroll(random.randint(-3, 3))  # Scroll up or down randomly between -3 and 3 "clicks"

    # Wait for a random time between 1 and 3 seconds
    time.sleep(random.uniform(1, 3))
