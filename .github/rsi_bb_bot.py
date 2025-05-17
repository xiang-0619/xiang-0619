import requests, hmac, hashlib, time, json

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"

def sign(params, secret):
    qs = '&'.join([f"{k}={params[k]}" for k in sorted(params)])
    return hmac.new(secret.encode(), qs.encode(), hashlib.sha256).hexdigest()

def place_order():
    base_url = "https://open-api.bingx.com/openApi/swap/v2/trade/order"
    params = {
        "symbol": "BTC-USDT",
        "side": "BUY",
        "price": "30000",  # 可修改為實際價格策略
        "quantity": "0.001",
        "tradeType": "LONG",
        "timestamp": str(int(time.time() * 1000))
    }
    params["signature"] = sign(params, API_SECRET)
    headers = {"X-BX-APIKEY": API_KEY}
    res = requests.post(base_url, headers=headers, data=params)
    print(res.text)

place_order()
