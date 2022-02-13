# Test-task-usps
Task conditions:
Using python and the requests library, write a scraper that reads a CSV file of addresses, and submits them to this website to check if they are valid or not:
https://tools.usps.com/zip-code-lookup.htm?byaddress
Your output should be the same CSV file as the input, but with an additional column added to it that displays if the address is valid. 
Please note you can also use other python libraries than the requests library, but your code must use the requests library.
The input data can be downloaded from file: Python Quiz Input - Sheet1.csv
## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
   Recommended using a Python virtual environment. And install all requirements.
   ```
   pip install -r requirements.txt
   ```
1. Create .env file and write to it your USERID, that you get on email from USPS.
   ```
   touch .env
   echo USPS_USERID='"your USERID"' >> .env
   ```
1. Finally run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   python3 check_adress_validations.py
   ```
