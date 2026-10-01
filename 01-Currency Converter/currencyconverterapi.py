import requests
while True:
    try:
        amount = float(input("Enter amount you want to convert: "))   
        if amount < 0:
            print("Enter positive amount.")
            continue
        break
    except ValueError:
            print("Enter amount in numbers.") 
            continue
fromcurr = input("From currency: ").upper()
tocurr = input("To currency: ").upper()

try:
    url = f"https://open.er-api.com/v6/latest/{fromcurr}"
    response = requests.get(url, timeout=5)


    if response.status_code == 200:

        data = response.json()

        if tocurr in data["rates"]:
            exchangerates = data["rates"][tocurr]
            finaloutput = amount * exchangerates
            print(f"{amount} {fromcurr} = {finaloutput:.2f} {tocurr}")
        else:
            print("Invalid Target Currency.")
    elif response.status_code == 404:
        print("Not found")
    else:
        print("Something went wrong with the currency converter API.")
except requests.exceptions.ConnectionError:
    print("Internet/API Connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException:
    print("Other request related problem.")