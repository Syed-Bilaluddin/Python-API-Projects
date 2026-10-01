import requests
import json
try:
    username = input("Enter repository to search: ")
    parameters={
        "q": username
    }
    url = f"https://api.github.com/search/repositories"
    response = requests.get(url, params=parameters, timeout=5)
    if response.status_code == 200:
        data = response.json()
        repositories = data["items"]
        
        if not repositories:
            print("No repository found.")
        else:
            for repo in repositories[:5]:
                name = repo["name"]
                owner = repo["owner"]["login"]
                desc = repo["description"]
                st_count = repo["stargazers_count"]
                html_url = repo["html_url"]

                print(f"Name: {name}")
                print(f"Owner: {owner}")
                print(f"Description: {desc}")
                print(f"Stargazers Count: {st_count}")
                print(f"HTML URL: {html_url}\n")
    elif response.status_code == 404:
        print("Username not found")
except requests.exceptions.ConnectionError:
    print("Internet/API Connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException:
    print("Other request related problem.")