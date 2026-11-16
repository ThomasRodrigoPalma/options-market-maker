import requests

response = requests.get('https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option')
data = response.json()
options = data['result']

print(f'Number of options available: {len(options)}')
print(f'First option: {options[0]}')