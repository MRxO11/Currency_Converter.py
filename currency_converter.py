from requests import get
from pprint import PrettyPrinter

API_KEY =  "8ad9c53e84ca0740a830230f"

printer = PrettyPrinter()

def get_currencies():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    data = get(url).json()

    return data

def exchange_rate(currency1, currency2):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency1}/{currency2}"
    data = get(url).json()
    

    rate = data['conversion_rate']
    print(f'{currency1} -> {currency2} = {rate}')
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate == None:
        return "Invalid currency"
    else:
        try:
            amount = float(amount)
        except:
            return "Invalid amount"

    converted_amount = amount * rate
    print(f'{amount}, {currency1} is equal to {converted_amount}, {currency2}')
    return converted_amount

def main():
    currencies = get_currencies()

    print(" Welcome to currency converter!!!")
    print(" Commands are....")
    print(" Enter  List ➡️   to list all currency.")
    print("Enter Convert ➡️   to convert the currency.")
    print("Enter Rate ➡️   to get the exhange rate of two currency. ")
    print()

    while True:
        command = input(' Enter the command(q to quit.) ').lower()
        if command =='q':
            break
        elif command == 'list':
            printer.pprint(currencies)
        elif command == 'convert':
            currency1 = input(" Enter the base currency id: ").upper()
            currency2 = input(" Enter the target currency id: ").upper()
            amount = input(f" Enter the amount to convert in {currency1}: ")
            convert(currency1, currency2, amount)
        elif command == 'rate':
            currency1 = input(" Enter the base currency id: ").upper()
            currency2 = input(" Enter the target currency id: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print(" Invalid command. Try again.")
            
main()