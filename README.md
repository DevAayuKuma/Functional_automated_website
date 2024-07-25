Project Title: Web Text Extraction and Verification with Selenium

Description:
This Python script utilizes Selenium WebDriver to automate the following tasks:

Invoking a website: Opens a specified website using the chosen WebDriver.
Selecting search text: Locates the search bar element and enters a search query.
Grabbing on-screen text: Extracts the relevant text displayed on the search results page.
Storing text in a list: Creates a list to store the extracted text for comparison.
Comparing with expected list: Compares the extracted text list with a pre-defined expected list of results.
Verification using assertions: Uses Python's assert statements to verify if the extracted text matches the expected results.

Requirements:
Python 3.x
Selenium (installation: pip install selenium)
WebDriver (download and configure the driver for your chosen browser from https://www.selenium.dev/documentation/webdriver/)

Instructions:
Install dependencies: Run pip install selenium in your terminal.
Download and configure WebDriver: Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox) 
and configure its path in your script (see code for guidance).
Update script variables: Replace placeholders in the script with your desired website URL, search query, and expected text list.

Usage:
Save the script as a Python file (e.g., web_text_extraction.py).
Run the script from your terminal: python web_text_extraction.py

Expected Behavior:
The script will open the website, enter the search query, extract the on-screen text, compare it with the expected list, 
and display verification messages using assertions. If the extracted text matches the expected results, the script will print success messages. 
If there are any discrepancies, the script will print error messages indicating mismatches.
