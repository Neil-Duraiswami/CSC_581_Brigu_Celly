# Simple Web Automation Task

This script automates the process of searching for a product on Amazon and retrieving the top 5 product names, prices, and ratings.

## Requirements
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver

## Setup
1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install Selenium WebDriver by running `pip install selenium` in your command line.
3. Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's accessible in your system's PATH.

## Running the Script
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.
3. Open a terminal or command prompt in this directory.
4. Run the script by executing `python webAutomation.py` and follow the prompts.

## Script Details
- The script opens a Chrome browser and navigates to Amazon's homepage.
- It searches for a predefined product term (e.g., "wireless headphones") and retrieves the top 5 product names, prices, and ratings.
- If fewer than 5 products are found, it prints the available products.
- Finally, the browser is closed automatically.

## Bonus Challenge
- The script handles situations where fewer than 5 products are found.
- It also captures and prints product ratings along with names and prices.

## Author
- Neil Duraiswami

