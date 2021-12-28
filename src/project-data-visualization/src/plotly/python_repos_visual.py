import requests

from plotly.graph_objs import Bar
from plotly import offline

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names = [repo['name'] for repo in repo_dicts]
repo_stars = [repo['stargazers_count'] for repo in repo_dicts]
repo_owners = [repo['owner']['login'] for repo in repo_dicts]
repo_description = [repo['description'] for repo in repo_dicts]
labels = [f"{owner}<br />{description}" for owner, description in
          zip(repo_owners, repo_description)]
repo_urls = [repo['html_url'] for repo in repo_dicts]
repo_links = [f"<a href='{url}'>{name}</a>" for url, name in
              zip(repo_urls, repo_names)]

# make visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': repo_stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most starred Python projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='graphs/python_repos.html')