import requests
import sys


if len(sys.argv) == 2:
    try:
        n= float(sys.argv[1])
    except ValueError:
        sys.exit("CLI arg is not a number")

elif len(sys.argv) == 1:
    sys.exit("Missing CLI argument")

else:
    sys.exit("Too many args")
    

try:
    response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourAPIKey')
    o = response.json()

    p = float(o['data']['priceUsd'])

    print(f'${n*p:,.4f}')
    

except requests.RequestException:                      
    print('Error')