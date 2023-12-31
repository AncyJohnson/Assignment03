from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Selenium web driver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed and in PATH
driver.get("https://www.youtube.com")

# Search for biryani recipe
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("biryani recipe")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load
search_results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "video-title"))
)

# Click on the first video
if search_results:
    first_video = search_results[0]
    first_video.click()

    # Wait for the video to load
    time.sleep(5)

    # Find the video player element
    video_player = driver.find_element(By.TAG_NAME, "video")

    # Pause the video
    driver.execute_script("arguments[0].pause();", video_player)
    print("Video paused.")

    # Wait for 3 seconds
    time.sleep(3)

    # Play the video
    driver.execute_script("arguments[0].play();", video_player)
    print("Video played.")

    # Wait for 3 seconds
    time.sleep(3)

    # Mute the video
    driver.execute_script("arguments[0].muted = true;", video_player)
    print("Video muted.")

    # Wait for 3 seconds
    time.sleep(3)

    # Unmute the video
    driver.execute_script("arguments[0].muted = false;", video_player)
    print("Video unmuted.")

    # Wait for 3 seconds
    time.sleep(3)

# Close the browser
driver.quit()
