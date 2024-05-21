from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.os_manager import ChromeType
import os
import time
from selenium.webdriver.support import expected_conditions as EC

# Specify the desired browser version
browser_version = "123.0.6312.122"
os.environ["CHROMEDRIVER_VERSION"] = browser_version

# Set the path to the ChromeDriver executable
chrome_driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()

# Create a ChromeDriver instance
driver = webdriver.Chrome(service=Service(chrome_driver_path))
# Maximize the browser window
driver.maximize_window()
# Use the driver to navigate to a website, interact with elements, etc.
driver.get("https://www.automationexercise.com/")

print(driver.title)
# Click on the Sign-In button
sign_in_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]")))
sign_in_button.click()

# Enter the username
username_input = driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")
username_input.send_keys("qat@mailinator.com")

# Enter the password
password_input = driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")
password_input.send_keys("123456")
# Submit the form
password_input.send_keys(Keys.RETURN)

# Find the elements containing the featured items
items = driver.find_elements(By.CSS_SELECTOR, ".features_items .col-sm-4")
print(items)
# Create a list to store item information
item_info = []

# Iterate through each item to extract label and price
for item in items:
    label = item.find_element(By.CSS_SELECTOR, ".productinfo p").text
    price = item.find_element(By.CSS_SELECTOR, ".productinfo h2").text
    # Remove the 'Rs.' prefix from the price and convert it to a float for sorting
    price = float(price.replace('Rs. ', ''))
    item_info.append({"label": label, "price": price})

# Sort the items by price
sorted_items = sorted(item_info, key=lambda x: x["price"])

# Print the sorted list of items with their labels and prices
print("Sorted Items (Low to High):")
for item in sorted_items:
    print(f"{item['label']} - Rs. {item['price']}")


# Navigate to Women >> Dress >> Women – Tops Products
women_menu = driver.find_element(By.XPATH, "//a[@data-toggle='collapse'][@href='#Women']")
women_menu.click()
time.sleep(1)


women_tops_submenu = driver.find_element(By.XPATH, "//div[@id='Women']//a[contains(text(), 'Tops')]")
women_tops_submenu.click()
time.sleep(2)

# Add Fancy Green Top to cart
fancy_green_top = driver.find_element(By.XPATH, "//div[@class='productinfo text-center']/p[contains(text(), 'Fancy Green Top')]/following-sibling::a[contains(@class, 'add-to-cart')]")
fancy_green_top.click()
time.sleep(2)

# Close modal if it appears
try:
    driver.find_element(By.CLASS_NAME, "close-modal").click()
    time.sleep(2)
except:
    pass

# Add Summer White Top to cart
summer_white_top = driver.find_element(By.XPATH, "//p[text()='Summer White Top']/following-sibling::a")
# Scroll the button into view
driver.execute_script("arguments[0].scrollIntoView();", summer_white_top)
summer_white_top.click()
time.sleep(2)

# Close modal if it appears
try:
    driver.find_element(By.CLASS_NAME, "close-modal").click()
    time.sleep(2)
except:
    pass
# View cart and proceed to checkout
view_cart = driver.find_element(By.XPATH, "//a[@href='/view_cart']")
view_cart.click()
time.sleep(2)

proceed_to_checkout = driver.find_element(By.XPATH, "/html/body/section/div/section/div[1]/div/div/a")
proceed_to_checkout.click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Add comments and place order
comments = driver.find_element(By.XPATH, "//*[@id='ordermsg']/textarea")
comments.send_keys("Order placed.")
place_order = driver.find_element(By.XPATH, "/html/body/section/div/div[7]/a")
place_order.click()
time.sleep(5)

# Enter card details and confirm order
card_name = driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(2) > div > input")
card_name.send_keys("Test Card")
card_number = driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(3) > div > input")
card_number.send_keys("4100000000000000")
cvc = driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[1]/input")
cvc.send_keys("123")
expiry = driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[2]/input")
expiry.send_keys("01/1900")
expiry = driver.find_element(By.XPATH, "//*[@id='payment-form']/div[3]/div[3]/input")
expiry.send_keys("2025")
time.sleep(3)
# Confirm order
confirm_order = driver.find_element(By.ID, "submit")
confirm_order.click()

# Ensure order has been placed
order_confirmation = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/p").text
print(order_confirmation)

time.sleep(3)
# Close the browser
driver.quit()
