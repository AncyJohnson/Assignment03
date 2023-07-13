from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Find and select Veena's Curry World video
for result in search_results:
    if "Veena's Curry World" in result.text:
        result.click()
        break

# Close the browser
driver.quit()
