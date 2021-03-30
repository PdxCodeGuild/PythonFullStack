



import requests
import json






def load_country_currency_codes():
    # https://restcountries.eu/#api-endpoints-all

    # country_currency_codes = {
    #     'Afghanistan': ['AFN'],
    #     'Åland Islands': ['EUR'],
    # }
    country_currency_codes = {}

    response = requests.get('https://restcountries.eu/rest/v2/all')

    countries = response.json()
    # countries = json.loads(response.text)

    # print(countries[0]['name'])
    # loop over our list of dictionaries (that represent countrie)
    for country in countries:
        # for each country, get the name and currency code
        name = country['name']

        # currency_codes = [currency['code'] for currency in country['currencies'] if currency['code'] not in [None, '(none)']]    

        currency_codes = []
        currencies = country['currencies'] # list of dictionaries
        for currency in currencies:
            currency_code = currency['code']
            if currency_code not in [None, '(none)']:
                currency_codes.append(currency_code)
        # print(name, currency_codes)
        country_currency_codes[name] = currency_codes
        # currency_code = country['currencies'][0]['code']
        # if len(country['currencies']) > 1:
        #     print('omigosh, ' + name + ' has ' + str(len(country['currencies'])) + ' currencies')
        

    return country_currency_codes


def get_exchange_rate(input_currency_code, output_currency_code):
    # https://api.exchangeratesapi.io/latest?base=USD
    response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': input_currency_code})
    rates = response.json()['rates']
    if output_country_currency_code not in rates:
        return None
    return rates[output_currency_code]
    

country_currency_codes = load_country_currency_codes()

# for country_name in country_currency_codes:
#     # if country_name.lower().startswith('u'):
#     if 'the' in country_name.lower():
#         print(country_name)


# get the input country from the user
input_country = input('Please enter your starting country: ').title().strip().replace('Of', 'of').replace('The', 'the')
# figure out the currency for the given country
if input_country not in country_currency_codes:
    print('Not a valid option, please see list of countries:')
    print('\n'.join(country_currency_codes.keys()))
    # for country_name in country_currency_codes:
    #     print(country_name)
    exit()

input_country_currency_code = country_currency_codes[input_country][0]



# get the input amount from the user
input_amount = float(input('Please enter your starting amount: '))


# get the output currency from the user
output_country = input('Please enter your ending country: ').title().strip().replace('Of', 'of').replace('The', 'the')
# figure out the currency for the given country
if output_country not in country_currency_codes:
    print('Not a valid option, please see list of countries:')
    print('\n'.join(country_currency_codes.keys()))
    # for country_name in country_currency_codes:
    #     print(country_name)
    exit()

output_country_currency_code = country_currency_codes[output_country][0]

# calculate the output amount and show it to the user
# print(input_amount)
# print(input_country)
# print(input_country_currency_code)
# print(output_country)
# print(output_country_currency_code)

exchange_rate = get_exchange_rate(input_country_currency_code, output_country_currency_code)
# print(exchange_rate)

output_amount = round(exchange_rate*input_amount, 2)
print(f'{input_amount} {input_country_currency_code} = {output_amount} {output_country_currency_code}')






