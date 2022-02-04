import logging
import os
from kiteconnect import KiteConnect
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect()
kite.login(os.getenv("USER_ID"), os.getenv("USER_PASSWORD"), os.getenv("USER_PIN"))
print(kite.profile())
kite.logout()
