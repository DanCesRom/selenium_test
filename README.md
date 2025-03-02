# Multi-Browser Automated Testing for Pokémon TCG Web App

This project automates the testing of a Pokémon TCG web application using Selenium WebDriver in Chrome, Firefox, and Edge. The script performs user interactions such as logging in, selecting filters, adding cards, and verifying results.

## Features
- **Cross-browser testing**: Runs on Chrome, Firefox, and Edge.
- **Automated form interactions**: Selects set name, regulation, and rarity.
- **Randomized card selection**: Picks a random number of cards and quantities.
- **Screenshot capture**: Saves a screenshot after test execution.
- **Database clearing**: Attempts to clear the database after the last test.

## Requirements
- Python 3.x
- Selenium WebDriver
- WebDriver executables for Chrome, Firefox, and Edge

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/DanCesRom/selenium_test.git
   cd your-repo
2. Install dependencies:
pip install selenium

3.Ensure you have the necessary WebDriver executables:
ChromeDriver
GeckoDriver (Firefox)
EdgeDriver

**Usage**
Run the script:
python test_script.py

The script will:

1.Open the web app in each browser.
2.Log in using the predefined password.
3.Select filters and add cards.
4.Navigate to the "Owned" page.
5.Capture a screenshot of the results.
6.Clear the database (only in Edge).

**Notes**
Adjust time.sleep() values if needed for slow-loading pages.
The script assumes the web app elements remain consistent.
Ensure your chromedriver, geckodriver, and msedgedriver are added to your system PATH.
