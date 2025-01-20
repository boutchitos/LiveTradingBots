import ccxt
import json
from collections import namedtuple
from main_account_auth import auth_params


Candle = namedtuple("Candle", ["timestamp", "open", "high", "low", "close", "volume"])


def dump(response):
    print(json.dumps(response, indent=4))


if __name__ == "__main__":
    params = {}
    params.update(auth_params)
    params.update(
        {
            "headers": {
                "locale": "en-US",
            },
            "options": {"defaultType": "swap", "productType": "SUSDT-FUTURES"},
        }
    )
    bitget = ccxt.bitget(params)
    bitget.set_sandbox_mode(True)

    bitget.load_markets()

    # 1- avoir le prix avec une candle. Peut etre en faire le EMA aussi.
    candles = [
        Candle(*candle)
        for candle in bitget.fetch_ohlcv("SBTC/SUSDT:SUSDT", "15m", limit=15)
    ]
    dump(candles[0].open)
    dump(candles[-1].close)
    # 2- Me faire un band à 0.03 long ou short
    # 3- programmer le TP au EMA, SL à 0.2.
