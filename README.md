# Code Wars Profile Scraper

This is a web scraper written in python to scrape the profile of a user on code wars(a competitive programming website). Although the CodeWars API is publicly available I made this scraper just for the love of scraping.
## See it in action
![cowaps in action](https://raw.githubusercontent.com/palash25/CoWaPS/master/assets/cowaps.gif)

### Requirements
You need **requests**, **BeautifulSoup** and **texttable** to run this script.

## Installation
Run the following commands on your terminal

### 1. System-wide installation
#### 1. Requests
Using apt-get:
`$ sudo apt-get install python3-requests`

Using pip:
`$ pip3 install requests`

#### 2. BeautifulSoup
Using apt-get:
`$ sudo apt-get install python3-bs4`

Using pip:
`$ pip3 install beautifulsoup4`

#### 3. TextTable
Using apt-get:
`$ sudo apt-get install python3-texttable`

Using pip:
`$ pip3 install texttable`

### 2. Installation using virtualenv
Fisrt you need to install virtualenv, if you don't already have one. Install it using the following command:

`$ python3 -m pip3 install --user virtualenv`

Then you need to create a virtual environment. To create a virtual environment, go to your project’s directory and run virtualenv using the following command:

`$ python3 -m virtualenv env`

Before you can start installing or using packages in your virtualenv you’ll need to activate it. Run the following command to activate virtualenv:

`$ source env/bin/activate` 

Now, to install the required packages follow the instructions as mentioned under the section `System-wide installation`.

**Note:**
1. It is recommended to run `sudo apt-get update` before running the above commands.
2. If you don't have python3/pip3 installed, replace `python3`/`pip3` with `python`/`pip` and run the command.
3. Still confused how to install? Google your questions. :wink:
