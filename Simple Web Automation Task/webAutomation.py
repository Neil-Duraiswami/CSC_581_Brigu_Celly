# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the function to search for a product and retrieve details
def search_amazon(search_term):
    # Initialize the WebDriver (assuming you're using Chrome)
    driver = webdriver.Chrome()
    
    # Navigate to Amazon's homepage
    driver.get("https://www.amazon.com")
    
    try:
        # Find the search bar and input the search term
        search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_bar.clear()
        search_bar.send_keys(search_term)
        
        # Submit the search
        search_bar.submit()
        
        # Wait for search results to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")))
        
        # Extract the names, prices, and ratings of the products
        product_names = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
        product_prices = driver.find_elements(By.CSS_SELECTOR, "span.a-price span.a-offscreen")
        product_ratings = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result'] span.a-icon-alt")
        
        # Print each product name, price, and rating (if available)
        for i in range(min(5, len(product_names))):
            name = product_names[i].text
            price = product_prices[i].text
            rating = product_ratings[i].text if i < len(product_ratings) else "No rating available"
            print(f"{name} - {price} - {rating}")
    
    finally:
        # Close the browser
        driver.quit()

# Call the function with the predefined search term
search_amazon("wireless headphones")
