import requests

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# explore information about the repositories
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# examine the first repository
repo_first = repo_dicts[0]
# print(f"\nKeys: {len(repo_first)}")
# for key in sorted(repo_first.keys()):
#     print(key)

print("\nSelected information about each repository:")
for repo in repo_dicts:
    print(f"\nName: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository URL: {repo['html_url']}")
    # print(f"Created: {repo['created_at']}")
    # print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}")