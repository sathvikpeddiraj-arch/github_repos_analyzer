#%%
import requests
import csv

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    

    data = response.json()

    sorted_data = sorted(
        data,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

    with open("repositories.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["name", "stars", "language"]
        )

        writer.writeheader()

        for repo in sorted_data:

            if repo["stargazers_count"] > 10:

                print(
                    f"{repo['name']} | "
                    f"Stars: {repo['stargazers_count']} | "
                    f"Language: {repo['language'] or 'Not specified'}"
                )

                writer.writerow({
                    "name": repo["name"],
                    "stars": repo["stargazers_count"],
                    "language": repo["language"] or "Not specified"
                })

    print("CSV report saved successfully!")

else:
    print(f"Failed with status code {response.status_code}")



# %%
