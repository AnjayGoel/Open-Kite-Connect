import logging
import os

from dotenv import load_dotenv

from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

load_dotenv()


kite = KiteConnect()
kite.login(os.getenv("USER_ID"), os.getenv("USER_PASSWORD"), os.getenv("USER_PIN"))

# Place single-leg gtt order - https://kite.trade/docs/connect/v3/gtt/#single
try:
    order_single = [{
        "exchange": "NSE",
        "tradingsymbol": "SBIN",
        "transaction_type": kite.TRANSACTION_TYPE_BUY,
        "quantity": 1,
        "order_type": "LIMIT",
        "product": "CNC",
        "price": 470,
    }]
    single_gtt = kite.place_gtt(trigger_type=kite.GTT_TYPE_SINGLE, tradingsymbol="SBIN", exchange="NSE",
                                trigger_values=[470], last_price=473, orders=order_single)
    logging.info("single leg gtt order trigger_id : {}".format(single_gtt['trigger_id']))
except Exception as e:
    logging.info("Error placing single leg gtt order: {}".format(e))

# Place two-leg(OCO) gtt order - https://kite.trade/docs/connect/v3/gtt/#two-leg
try:
    order_oco = [{
        "exchange": "NSE",
        "tradingsymbol": "SBIN",
        "transaction_type": kite.TRANSACTION_TYPE_SELL,
        "quantity": 1,
        "order_type": "LIMIT",
        "product": "CNC",
        "price": 470
    }, {
        "exchange": "NSE",
        "tradingsymbol": "SBIN",
        "transaction_type": kite.TRANSACTION_TYPE_SELL,
        "quantity": 1,
        "order_type": "LIMIT",
        "product": "CNC",
        "price": 480
    }]
    gtt_oco = kite.place_gtt(trigger_type=kite.GTT_TYPE_OCO, tradingsymbol="SBIN", exchange="NSE",
                             trigger_values=[470, 480], last_price=473, orders=order_oco)
    logging.info("GTT OCO trigger_id : {}".format(gtt_oco['trigger_id']))
except Exception as e:
    logging.info("Error placing gtt oco order: {}".format(e))
