import requests
try:
    response = requests.get("https://zenquotes.io/api/random", timeout=5)
    if response.status_code == 200:

        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        print(quote)
        print(author)
except requests.exceptions.ConnectionError:
    print("Internet/API Connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException:
    print("Other request related problem.")