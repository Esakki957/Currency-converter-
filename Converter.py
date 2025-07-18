import requests

def convert_currency(amount, from_currency, to_currency):
    url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("result"):
        print(f"\n💱 {amount} {from_currency.upper()} = {data['result']} {to_currency.upper()}")
    else:
        print("\n❌ Conversion failed.")

# --- User input version ---
if __name__ == "__main__":
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD): ")
        to_currency = input("To currency (e.g., INR): ")

        convert_currency(amount, from_currency, to_currency)
    except ValueError:
        print("❌ Invalid amount entered.")
