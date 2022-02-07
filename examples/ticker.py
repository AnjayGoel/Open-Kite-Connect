###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Zerodha Technology Pvt. Ltd.
#
# This example shows how to subscribe and get ticks from Kite Connect ticker,
# For more info read documentation - https://kite.trade/docs/connect/v1/#streaming-websocket
###############################################################################
from dotenv import load_dotenv
import logging
from kiteconnect import KiteTicker, KiteConnect
import os

load_dotenv()
logging.basicConfig(level=logging.DEBUG)

# Initialise
kite = KiteConnect(debug=True)
kite.login(os.getenv("USER_ID"), os.getenv("USER_PASSWORD"), os.getenv("USER_PIN"))
kws = KiteTicker(kite.access_token)


def on_ticks(ws, ticks):  # noqa
    # Callback to receive ticks.
    logging.info("Ticks: {}".format(ticks))


def on_connect(ws, response):  # noqa
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([738561, 5633])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [738561])


def on_order_update(ws, data):
    logging.debug("Order update : {}".format(data))


# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_order_update = on_order_update

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
