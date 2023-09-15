from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
import sys

# flag to determine if timer should keep running
timer_running = True

def format_time(seconds):
    # converts the seconds to minutes and seconds
    minutes = int(seconds // 60)
    seconds_remainder = seconds % 60
    return f"{minutes} minute{'s' if minutes != 1 else ''} {seconds_remainder:.4f} seconds"

def timer_function(start_time):
    while timer_running:
        time_elapsed = time.time() - start_time
        sys.stdout.write(f"\rTime elapsed: {format_time(time_elapsed)}")
        sys.stdout.flush()
        time.sleep(1)  # Update the console every second

def start_quick_draw():
    global timer_running

    browser = webdriver.Chrome()

    try:
        browser.get('https://quickdraw.withgoogle.com/')

        browser.maximize_window()

        # Wait for the page to load and check if the cookie notification is present
        try:
            # waits for up to 10 seconds for the cookie notification button to be visible
            cookie_button = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'glue-cookie-notification-bar__accept'))
            )
            cookie_button.click()
        except:
            pass  # If the button is not found, move on

        # Wait for "Let's draw" button to be clickable
        button_play = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'button-play'))
        )

        print("Please click on 'Let's draw' when ready...")

        # wait up to 10 minutes (600 seconds) for the "Let's Draw!" button to be not visible.
        WebDriverWait(browser, 600).until_not(EC.visibility_of_element_located((By.ID, 'button-play')))

        print("Drawing has started...")

        # Start the timer
        start_time = time.time()
        timer_thread = threading.Thread(target=timer_function, args=(start_time,))
        timer_thread.start()

        # wait up to 3 minutes for the "Play Again" button to be visible.
        WebDriverWait(browser, 180).until(EC.visibility_of_element_located((By.ID, 'button-timesup-play')))

        timer_running = False
        timer_thread.join()

        elapsed_time = time.time() - start_time
        print(f"\nTotal drawing time: {format_time(elapsed_time)}")

        # Keep the browser window open
        input("Press Enter to close the browser and exit the script...")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        browser.quit()

if __name__ == "__main__":
    start_quick_draw()
