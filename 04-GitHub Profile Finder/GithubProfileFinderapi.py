import requests
try:
    username = input("Enter Your GitHub Username: ")

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()

        login = data["login"]
        followers = data["followers"]
        following = data["following"]
        public_repositories = data["public_repos"]
        html_url = data["html_url"]

        print(f"Username: {login}")
        print(f"Followers: {followers}")
        print(f"Following: {following}")
        print(f"Public Repositories: {public_repositories}")
        print(f"Profile Url: {html_url}")
    
    elif response.status_code == 404:
        print("GitHub Username don't exist.")

except requests.exceptions.ConnectionError:
    print("Internet/API Connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException:
    print("Other request related problem.")