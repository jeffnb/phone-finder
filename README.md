[![Build Status](https://travis-ci.org/jeffnb/phone-finder.svg?branch=master)](https://travis-ci.org/jeffnb/phone-finder)

# Phone Number Finder

## Description

This is a simple web service with 1 page and 1 form.  It simply allows the user to paste in any text
into the form field and submit.  The system will then extract all phone numbers in a variety of formats 
and list them out below the form.

## Demo Site
The application has been deployed to heroku and is available without installation
[Demo Site](https://stormy-brushlands-12573.herokuapp.com/)

## Install and Run
* Clone the repository to a directory
* Optional but recommended: Create a virtual environment
* Run `pip3 install -r requirements`
* Run `python3 phone-finder.py`
* Should display `Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
* Go to that url in the browser

## Testing
* Nose tests has been install
* Run `nosetests` in the directory

## The Stack
This application is written with python and flask.  [Flask](http://flask.pocoo.org/docs/0.11/) was chosen for its simplicity as a micro-framework given that 
the web application only needed 1 route to process the input from the user.  Additionally, the 
form is extremely simplistic requiring very little validation.  The core technology driving the application is
the regex that allows parsing of phone numbers in the block of text provided.

## Number Caveats
A few known formats of numbers that might be parsed in an undesirable way.
* No Area Code: Currently, the system will not extract numbers without an area code
* Extra numbers: If the last block of 4 numbers has more than 4 numbers it will simply match the first 4
