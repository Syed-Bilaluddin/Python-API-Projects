import requests
import json
try:
    keyword = input("Enter repository to search: ")
    while True:
        try:
            min_stars = int(input("Enter minimum stars: "))
            if min_stars < 0:
                print("Enter positive numbers.")
                continue
            break
        except ValueError:
            print("Enter in numbers: ")
            continue
        

    language = input("Enter programming language (or press Enter for any): ").strip().lower()
    url = f"https://api.github.com/search/repositories"
    repositories = []

    for page in range(1, 4):
        parameters={
            "q": keyword,
            "per_page": 30,
            "page": page    
        }
        response = requests.get(url, params=parameters, timeout=5)
        if response.status_code == 200:
            data = response.json()
            page_repositories = data["items"]

            if not page_repositories:
                break
            repositories.extend(page_repositories)
        elif response.status_code == 403 or response.status_code == 429:
            print("GitHub may have rate-limited your requests.")
            break
        else:
            print(f"API request failed: {response.status_code}")
            break

    filtered_repositories = []
    for repo in repositories:
        if repo["stargazers_count"] >= min_stars and (
            not language or (repo["language"] and repo["language"].lower() == language.lower())):
            filtered_repositories.append(repo)
    print(f"Repositories before filtering: {len(repositories)}")
    print(f"Repositories after filtering: {len(filtered_repositories)}")

    filtered_repositories.sort(key=lambda repo: repo["stargazers_count"], reverse=True)

    unique_developers = {}
    for repo in filtered_repositories:
            
        repo_name = repo["name"]
        owner = repo["owner"]["login"]
        desc = repo["description"]
        stars = repo["stargazers_count"]
        repo_url = repo["html_url"]
        profile_url = repo["owner"]["html_url"]

        current_repo_details = {
            "name": repo_name,
            "owner": owner,
            "description": desc,
            "stars": stars,
            "repo url": repo_url,
            "profile url": profile_url
        }

        if owner not in unique_developers:
            unique_developers[owner] = {
                "owner name": owner,
                "profile url": profile_url,
                "repositories": [current_repo_details]
            }
        else:
            unique_developers[owner]["repositories"].append(current_repo_details)

    with open("developers_results.txt", "w", encoding="utf-8") as file:

        for ud, details in unique_developers.items():
            file.write(f"\nOwner: {ud}\n")
            file.write(f"Profile URL: {details['profile url']}\n")
            
            for repo in details["repositories"]:
                file.write(f"Repository: {repo['name']}\n")
                file.write(f"Description: {repo['description']}\n")
                file.write(f"Stars: {repo['stars']}\n")
                file.write(f"Repository URL: {repo['repo url']}\n\n")

    print(f"Successfully saved {len(unique_developers)} developers to developers_results.txt")

    multiple_owners = {
        owner: details
        for owner, details in unique_developers.items()
        if len(details["repositories"]) > 1
    }
    with open("developers_with_multiple_repositories.txt", "w", encoding="utf-8") as file:
        if multiple_owners:
            for owner, details in multiple_owners.items():
                file.write(f"\nOwner: {owner}\n")
                file.write(f"Profile URL: {details['profile url']}\n")
                file.write(f"Number of repositories: {len(details['repositories'])}\n")
                
                for repo in details["repositories"]:
                    file.write(f"   - {repo['name']} ({repo['stars']})\n")
                    file.write(f"     {repo['repo url']}\n\n")
                file.write("\n")
        else:
            file.write("No owners with multiple repositories found.\n")

    print(f"Found {len(multiple_owners)} developers with multiple repositories.")

   
except requests.exceptions.ConnectionError:
    print("Internet/API Connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.RequestException:
    print("Other request related problem.")