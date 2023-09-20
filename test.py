from selenium import webdriver
import time
import threading

def main():
    # Create a lock to synchronize access to the browser
    lock = threading.Lock()

    # Create a list to hold the browser instances
    browsers = []

    # Create 20 browser instances
    for i in range(20):
        # Create a new browser instance
        browser = webdriver.Chrome()

        # Add the browser instance to the list
        browsers.append(browser)

    # Open the web page
    for browser in browsers:
        browser.get("https://googlelungtung.glitch.me/")

    # Start all threads
    for browser in browsers:
        thread = threading.Thread(target=_run_thread, args=(lock, browser))
        thread.start()

    # Wait for all threads to finish
    for thread in threading.enumerate():
        thread.join()

    # Close all browsers
    for browser in browsers:
        browser.quit()

def _run_thread(lock, browser):
    # Lock the thread
    lock.acquire()

    image_urls = browser.find_elements_by_tag_name("body")
    # Unlock the thread
    lock.release()

if __name__ == "__main__":
    main()