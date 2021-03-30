




import requests


import colorama
colorama.init()


class QuoteAPI:
    def __init__(self):
        self.qotd_url = 'https://favqs.com/api/qotd'
        self.quote_history = []
    
    def get_qotd(self):
        response = requests.get(self.qotd_url)
        data = response.json()
        quote = {
            'body': data['quote']['body'],
            'author': data['quote']['author'],
            'tags': data['quote']['tags']
        }
        self.quote_history.append(quote)
        return quote
    
    def print_qotd(self):
        qotd = self.get_qotd()
        print(colorama.Fore.BLUE + '"' + qotd['body'] + '"' + colorama.Fore.CYAN + ' - ' + qotd['author'] + colorama.Style.RESET_ALL)
        print(colorama.Style.DIM + 'Tags: ' + ','.join(qotd['tags']))
    
    def get_quotes(self, filter='', page=1):
        params = {}
        if filter != '':
            params = {'filter': filter, 'page': page}
        response = requests.get('https://favqs.com/api/quotes/', params=params, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        data = response.json()
        output = []
        for quote in data['quotes']:
            output.append({
                'body': quote['body'],
                'author': quote['author'],
                'tags': quote['tags']
            })
        self.quote_history.extend(output)
        return output
    
    def get_all_quotes(self, filter):
        page = 1
        output = []
        while True:
            params = {'filter': filter, 'page': page}
            response = requests.get('https://favqs.com/api/quotes/', params=params, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            data = response.json()
            
            for quote in data['quotes']:
                output.append({
                    'body': quote['body'],
                    'author': quote['author'],
                    'tags': quote['tags']
                })
            
            if data['last_page']:
                break
            page += 1
            print(page)
        self.quote_history.extend(output)
        return output

        


# from quote_api import QuoteAPI
# import quote_api


quote_api = QuoteAPI() # instantiation, invoking the initializer to create an instance (object) of the class (blueprint)

qotd = quote_api.get_qotd()
qotd = quote_api.get_qotd()
qotd = quote_api.get_qotd()

print(quote_api.quote_history)

# quotes = quote_api.get_quotes('cat')
# print('got ' + str(len(quotes)) + ' quotes')
# print(quotes)

# print(colorama.Style.RESET_ALL)
# print(colorama.Fore.RED + colorama.Style.DIM + 'hello' + colorama.Style.NORMAL + 'hello' + colorama.Style.BRIGHT + 'hello')
