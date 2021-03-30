
import requests
import json

def get_currencies():
    url = 'https://api.exchangeratesapi.io/latest?base=USD'
    response = requests.get(url)
    data = response.json()
    return list(data['rates'].keys())


def get_country_currencies():
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url)
    countries = response.json()
    output = []
    for country in countries:
        output.append({
            'name': country['name'],
            'currencies': country['currencies']
        })
    return output



currencies = get_currencies()
country_currencies = get_country_currencies()
print(json.dumps(country_currencies, indent=4))

# [{'name': 'United States', 'currency': 'USD'}]

output = []
for currency in currencies:
    for country in country_currencies:
        currency_found = False
        for country_currency in country['currencies']:
            if country_currency['code'] == currency:
                output.append({
                    'name': country['name'],
                    'currency': currency
                })
                currency_found = True
                break
        if currency_found:
            break

print(json.dumps(output, indent=4))






