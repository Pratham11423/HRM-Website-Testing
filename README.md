# OrangeHRM Automation Testing using Python & Selenium

## Project Description
This project contains automated test scripts for the OrangeHRM web application. The purpose of this project is to automate the testing of various modules of the OrangeHRM system using Python and Selenium WebDriver.

OrangeHRM is a Human Resource Management system used for managing employee information, recruitment, leave management, and other HR-related processes. In this project, Selenium is used to simulate user actions on the website and validate different functionalities.

## Technologies Used
- Python
- Selenium WebDriver
- ChromeDriver
- PyTest / Unittest (if used)
- HTML Test Reports (optional)

## Features Tested
The automation scripts cover the following modules:

- Login functionality
- Dashboard verification
- Employee Management
- Logout functionality
- Navigation between different modules

## Project Structure
```
orangehrm-automation/
│
├── tests/
│   ├── test_login.py
│   ├── test_dashboard.py
│   └── test_logout.py
│
├── drivers/
│   └── chromedriver.exe
│
├── screenshots/
│
├── requirements.txt
└── README.md
```

## Prerequisites
Make sure the following are installed on your system:

- Python (3.x)
- Google Chrome Browser
- ChromeDriver
- pip (Python package manager)

## Installation
Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Running the Automation Tests
To run the test scripts, execute:

```bash
python test_login.py
```

or if using pytest:

```bash
pytest
```

## Test Scenario Example
Example test scenario for Login:

1. Open the OrangeHRM website
2. Enter valid username and password
3. Click the login button
4. Verify successful login and dashboard visibility

## Learning Outcome
This project helped in gaining practical experience in:

- Web automation using Selenium
- Writing automated test scripts in Python
- Locating web elements using XPath and CSS selectors
- Handling waits and browser interactions
- Basic automation testing concepts

## Author
Pratham Vishwakarma
