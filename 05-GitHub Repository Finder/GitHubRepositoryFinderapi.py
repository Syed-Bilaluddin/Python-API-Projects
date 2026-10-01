import requests
try:
    username = input("Enter Your GitHub Username: ")
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()
        print("===GITHUB REPOSITORIES===")
        for repo in data:
            name = repo["name"]
            desc = repo["description"]
            repository_url = repo["html_url"]               
            
            print(f"Name: {name}")
            print(f"Description: {desc}")
            print(f"Repository URL: {repository_url}\n")
    elif response.status_code == 404:
        print("Username don't exist.")
except requests.exceptions.ConnectionError:
    print("Internet/API Connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException:
    print("Other request related problem.")