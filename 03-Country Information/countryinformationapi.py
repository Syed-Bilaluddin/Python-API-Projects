from dotenv import load_dotenv
import os
import requests
load_dotenv()
api_key = os.getenv("COUNTRY_API_KEY")
try:
    country = input("Enter country name: ")

    headers={"Authorization": f"Bearer {api_key}"}
    url = f"https://api.restcountries.com/countries/v5/names.common/{country}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:

        data = response.json()
        if data["data"]["objects"]:
            country = data["data"]["objects"][0]["names"]["common"]
            region = data["data"]["objects"][0]["region"]
            continent = data["data"]["objects"][0]["continents"]
            population = data["data"]["objects"][0]["population"]
            capital = data["data"]["objects"][0]["capitals"][0]["name"]
            currency = data["data"]["objects"][0]["currencies"][0]["name"]
            
            print(f"Country: {country}")
            print(f"Region: {region}")
            print(f"Continent: {continent}")
            print(f"Population: {population}")
            print(f"Capital: {capital}")
            print(f"Currency: {currency}")
            print("Languages: ")
            for language in data["data"]["objects"][0]["languages"]:
                print(language["name"])
        else:
            print("Country Not Found.")
except requests.exceptions.ConnectionError:
    print("Internet/API Connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException:
    print("Other request related problem.")