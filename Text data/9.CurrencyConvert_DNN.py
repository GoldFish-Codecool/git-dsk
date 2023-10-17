from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    conversion_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * conversion_rate
    return converted_amount

amount = float(input("Enter the amount: "))
from_currency = input("Enter the from currency: ").upper()
to_currency = input("Enter the to currency: ").upper()

result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")
