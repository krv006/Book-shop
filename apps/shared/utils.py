import requests
from django.core.cache import cache


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


def get_currency():
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        exchange_rates = {item['Ccy']: float(item['Rate']) for item in data}
        exchange_rates['USD'] = 1
        usd_rate = exchange_rates.get('USD')
        print(f"USD narxi: {usd_rate}")
        return exchange_rates
    except (requests.RequestException, ValueError) as e:
        print(f"Xato: {e}")
        return {'USD': 1, 'UZS': 11500}


get_currency()
