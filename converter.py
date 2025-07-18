import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("result"):
        print(f"{amount} {from_currency} = {data['result']} {to_currency}")
    else:
        print("Conversion failed.")

# Example usage:
convert_currency(100, "USD", "INR")
