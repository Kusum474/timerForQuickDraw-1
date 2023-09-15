from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
import sys

# Global flag to determine if timer should keep running
timer_running = True

def format_time(seconds):
    """Convert a time value in seconds to a string in format 'X minutes Y.YYYY seconds'."""
    minutes = int(seconds // 60)
    seconds_remainder = seconds % 60
    return f"{minutes} minute{'s' if minutes != 1 else ''} {seconds_remainder:.4f} seconds"

def timer_function(start_time):
    while timer_running:
        elapsed_time = time.time() - start_time
        sys.stdout.write(f"\rTime elapsed: {format_time(elapsed_time)}")
        sys.stdout.flush()
        time.sleep(1)  # Update the console every second

def start_quick_draw():
    global timer_running

    # Open Google Chrome
    browser = webdriver.Chrome()

    try:
        # Navigate to Quick, Draw! website
        browser.get('https://quickdraw.withgoogle.com/')

        # Wait for the "Let's draw" button to be clickable
        button_play = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'button-play'))
        )

        print("Please click on 'Let's draw' when ready...")

        # Explicitly wait up to 10 minutes (600 seconds) for the "Let's Draw!" button to be not visible.
        WebDriverWait(browser, 600).until_not(EC.visibility_of_element_located((By.ID, 'button-play')))

        print("Drawing has started...")

        # Start the timer
        start_time = time.time()
        timer_thread = threading.Thread(target=timer_function, args=(start_time,))
        timer_thread.start()

        # Explicitly wait up to 3 minutes for the "Play Again" button to be visible.
        WebDriverWait(browser, 180).until(EC.visibility_of_element_located((By.ID, 'button-timesup-play')))

        keep_timer_running = False
        timer_thread.join()

        elapsed_time = time.time() - start_time
        print(f"\nTotal drawing time: {format_time(elapsed_time)}")

        # Keep the browser window open until the user decides to close it
        input("Press Enter to close the browser and exit the script...")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        browser.quit()

if __name__ == "__main__":
    start_quick_draw()
