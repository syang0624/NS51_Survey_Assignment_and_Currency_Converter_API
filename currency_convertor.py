#python www.exchangerate-api.com/
import os
os.system('pip install py-currency-converter')
from py_currency_converter import convert
print(convert(base='USD', amount=1, to=['KRW', 'EUR']))

#python API (default target currency as EUR)
os.system('pip install CurrencyConverter')
from currency_converter import CurrencyConverter
c = CurrencyConverter()
print(c.convert(100, 'EUR', 'USD'))
#fallback rate
from datetime import date
c = CurrencyConverter(fallback_on_wrong_date=True)
print(c.convert(100, 'EUR', 'USD', date=date(1986, 2, 2)))# fallback to 1999-01-04 as API has data from 1999-01-04.)