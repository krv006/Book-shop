import requests


def get_currency_rates():
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        usd_rate = None
        for currency in data:
            if currency['Ccy'] == 'USD':
                usd_rate = float(currency['Rate'])
                print(f"1 USD to UZS: {usd_rate} UZS")
                break
        if usd_rate:
            uzs_to_usd = 1 / usd_rate
            print(f"1 UZS to USD: {uzs_to_usd:.6f} USD")
        else:
            print("USD rate not found.")
    else:
        print("Error fetching currency rates.")


get_currency_rates()
