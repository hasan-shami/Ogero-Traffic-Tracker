# Ogero Traffic Tracker

Automatically logs your internet traffic consumption from the Ogero website into an Excel file. 


## Description

If you've ever wanted to log your internet traffic consumption (in Lebanon) periodically, this is the tool for you. This script logs into the Ogero website on every run, marks down your consumption information, and automatically updates an Excel file with information about your download and upload traffic, as well as extra consumption in order to estimate your fees. 

You will also be able to save information on past months and estimate days of the month where internet usage fluctuated.

## Installation/Dependencies

 - Anaconda distribution of Python 3.7
 - Selenium library on Python and Chrome extension, to scrape websites (make sure you install the appropriate versions)
 - xlsxwriter library on Python, to create and format Excel files
 - openpyxl library on Python, to edit existing Excel files and format them
 - datetime and os libraries on Python

## Future Steps

I want to amend the functionality of the project to work on other operating systems (using the pathlib library). I also want to create a tool that would periodically automate the running of the script on a remote machine. Some users have also reported that they have been facing issues with the CAPTCHA, which I hope to look into.

