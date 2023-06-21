import requests
import time

# global variables
api_key = "c56137cd-c117-4adf-89d0-6930f0d77b5d" # used for HTTP request with CMC
bot_token = "6165799318:AAE873TgKi8ncUGHdXLcJnC_jitHfXxGTAM" # used for communication with RossBTCUpdaterBot on TG
chat_id = "537855531"
threshold = 20000 # if BTC price < 20000, notification immediately deployed
time_interval = 10 * 60 # time in seconds between notifications

def get_bitcoin_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        # I need to finish Learn Python 3 before continuing, because this is dictionary stuff
    }