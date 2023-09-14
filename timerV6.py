import time
from selenium import webdriver
import threading

# Global stop flag for timer
stop_timer = False

def timer_function(start_time):
    global stop_timer
    while not stop_timer:
        elapsed_time = time.time() - start_time
        print(f"Time Elapsed: {elapsed_time:.2f} seconds")
        time.sleep(1)

def play_quick_draw():
    global stop_timer

    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()

    # Navigate to the Quick, Draw! website
    driver.get('https://quickdraw.withgoogle.com/')

    print("Please manually click the 'Let's Draw!' button when ready...")

    # Record the start time when the user clicks the button
    start_time = time.time()

    # Start the timer thread
    timer_thread = threading.Thread(target=timer_function, args=(start_time,))
    timer_thread.start()

    # Initialize a variable to keep track of the drawing count
    drawing_count = 0

    while drawing_count < 6:
        # Your code to interact with the game and draw goes here
        # You'll need to identify elements and perform actions (e.g., drawing)

        # Check if the drawing is complete (you may need to adjust this condition)
        if check_drawing_complete():
            drawing_count += 1
            print(f"Drawing {drawing_count} completed.")

    # Record the end time when the last page is launched
    end_time = time.time()

    driver.quit()

    # Stop the timer thread
    stop_timer = True
    timer_thread.join()

    # Calculate the total time taken
    total_time = end_time - start_time

    print(f"Total time taken for 6 drawings: {total_time:.4f} seconds")

def check_drawing_complete():
    # Implement your logic to check if the drawing is complete
    # Return True if complete, otherwise return False
    pass

if __name__ == "__main__":
    play_quick_draw()
