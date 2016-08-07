# brampton-transit-sms
Python scraper and web API for Brampton Transit's Next Ride service with SMS functionality. It looks like Brampton Transit already has this feature if you text/email their Next Ride email but it appears to be down or their service is just trash. 

## Scraper
* Data source: Next Ride's [mobile site] (http://nextride.brampton.ca/mob/SearchBy.aspx)

## API
### Requirements
* Python (`^2.7`)
* Flask (`^0.8`)
* ngrok 

## Getting started
* Clone project and cd into the directory

  `$ git clone https://github.com/dhyanpathak/brampton-transit-sms.git && cd brampton-transit-sms`
* Install Python requirements

  `$ pip install -r requirements.txt`
* Run the app on `localhost:5000` 

  `$ python run.py`
* Establish your local server for the app on the same listening port by running ngrok.exe
  
  `$ ngrok.exe http 5000`
  
  *For scaling, deploy the app on a [web server] (https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

## Usage
* Create a Twilio account and validate your phone number
* Configure your Twilio phone number to POST incoming messages to http://YOUR_NGROK_URL.ngrok.io/sms.
<img src="https://www.twilio.com/blog/wp-content/uploads/2016/07/1RhEjHZRQTLnrxUbH5RBwT2ektzSELAGLgzgw5w2sjvms9fpRewPZQuOVh9vw2yxbzUCZ1alNDvCh6M1NdQK5sfbyJGQayq-j0sNKCvMA-XrKNBPRlGSVAYKI8StIEG0tQB8XGU.png" width="600px" height="400px" />
* Text a stop number to your Twilio phone number. 

## Example
<img src="https://i.imgur.com/gktVG79.png" width="300px" height="600px" />

## Scaling (coming soon)
* Utilize the Twilio REST API to programmtically validate outbound caller IDs. This will allow multiple people to use one Twilio phone number.
* Deploy app on Heroku to handle more HTTP POSTs instead of running locally.
* Upgrade Twilio account and cover the expenses
<img src="https://i.gyazo.com/18718cc82cf14898f5c8786ae4193f26.png" width="700px" height="150px" />
