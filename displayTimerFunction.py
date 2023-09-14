import time

def display_timer():
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"Time Elapsed: {elapsed_time:.2f} seconds")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTimer stopped.")

display_timer()
