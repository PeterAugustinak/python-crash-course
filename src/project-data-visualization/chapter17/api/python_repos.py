import requests


def make_api_call(url):
    # make an API call and store the response
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)
    return response


def make_repo_dicts(response):
    # store API response in a variable
    response_dict = response.json()
    repo_dicts = response_dict['items']
    return repo_dicts


def print_info_about_items(repo_dicts):
    print("\nSelected information about each repository:")
    for repo in repo_dicts:
        print(f"\nName: {repo['name']}")
        print(f"Owner: {repo['owner']['login']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"Repository URL: {repo['html_url']}")
        # print(f"Created: {repo['created_at']}")
        # print(f"Updated: {repo['updated_at']}")
        print(f"Description: {repo['description']}")


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

if __name__ == '__main__':
    response = make_api_call(url)
    repo_dicts = make_repo_dicts(response)
    print_info_about_items(repo_dicts)