import requests

# Assuming that the API call might fail sometimes, retry until it succeeds.
while True:
    url = 'http://data.fixer.io/api/latest?access_key=213c949014296656544d13abdad7c41d&symbols=USD,GBP'
    response = requests.get(url)
    if response.status_code == 200:
        jsonResponse = response.json()
        # print(jsonResponse)

        # Reading USD and GBP rates relative to EUR 
        # Calculating USD/GBP rate (Base currency in free version of Fixer API is EUR)
        # Calculating  how much GBP would 100 USD buy
        EURUSD_rate = float(jsonResponse["rates"]["USD"])
        EURGBP_rate = float(jsonResponse["rates"]["GBP"])
        USDGBP_rate = EURGBP_rate / EURUSD_rate
        USD_100_buys = USDGBP_rate*100
        print ("100 USD will buy GBP: ",USD_100_buys)

        break

