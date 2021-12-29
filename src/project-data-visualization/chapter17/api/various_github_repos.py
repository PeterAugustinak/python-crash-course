# exercise 17-1

import requests

from plotly import offline


def create_visualization_for_language(language):
    """Uses all functions to create visualization for given language"""
    repo_dicts = make_repo_dict(language)
    if repo_dicts:
        data_to_vis = process_dict_result(repo_dicts)
        make_visualization(data_to_vis, language)
        print(f"\tVisualization for {language} generated!")
    else:
        print("\tNo data for visualization.")


def make_repo_dict(lang):
    """
    Based on language input calls GitHub API and returns dicts with most
    popular repositories on given language.
    """
    lang = lang.lower()
    print(f"\n{lang.upper()}")

    # make an API call and store the response
    url = f'https://api.github.com/search/repositories?q=language:' \
          f'{lang}&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        print(f"\tStatus code: {r.status_code}")
        # store API response in a variable
        response_dict = r.json()
        print(f"\tTotal repositories found: {response_dict['total_count']}")
        # explore information about the repositories in given language
        repo_dicts = response_dict['items']
        print(f"\tRepositories to process: {len(repo_dicts)}")
        return repo_dicts


def process_dict_result(repo_dicts):
    """Proces data for specific list of repositories by language"""
    repo_names = [repo['name'] for repo in repo_dicts]
    repo_stars = [repo['stargazers_count'] for repo in repo_dicts]
    repo_owners = [repo['owner']['login'] for repo in repo_dicts]
    repo_description = [repo['description'] for repo in repo_dicts]
    labels = [f"{owner}<br />{description}" for owner, description in
              zip(repo_owners, repo_description)]
    repo_urls = [repo['html_url'] for repo in repo_dicts]
    repo_links = [f"<a href='{url}'>{name}</a>" for url, name in
                  zip(repo_urls, repo_names)]

    data_to_vis = {
        'links': repo_links,
        'stars': repo_stars,
        'labels': labels
        }

    return data_to_vis


def make_visualization(data_to_vis, lang):
    """Based on given data makes visualization"""
    data = [{
        'type': 'bar',
        'x': data_to_vis.get('links'),
        'y': data_to_vis.get('stars'),
        'hovertext': data_to_vis.get('labels'),
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': f'Most starred {lang.title()} projects on GitHub',
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
    offline.plot(fig, filename=f'graphs/various_repos/'
                               f'{lang.lower()}_repos.html')


# CREATE VISUALIZATION
language_list = ['Python', 'JavaScript', 'Ruby', 'C', 'Java', 'Perl',
                 'Haskell', 'Go']

for language in language_list:
    create_visualization_for_language(language)

