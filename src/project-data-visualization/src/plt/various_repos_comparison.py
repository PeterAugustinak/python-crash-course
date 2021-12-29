# exercise 17-4

import requests
import operator

from plotly import offline


def create_language_comparison_visualization(lang_lst):
    """
    Checks total repos count for every language in a list and creates
    comparison chart
    """
    data_to_vis = {}
    for lang in lang_lst:
        total_repos = get_total_repos_count(lang)
        if total_repos:
            data_to_vis.update({lang: total_repos})

    data_to_vis = dict(sorted(data_to_vis.items(),
                              key=operator.itemgetter(1),
                              reverse=True))

    print(f"\nData to visualize: ")
    for key, value in data_to_vis.items():
        print(f"\t{key.title()}: {value}")

    make_visualization(data_to_vis)
    print(f"\tVisualization generated!")


def get_total_repos_count(lang):
    """
    Based on language input calls GitHub API and returns number of existing
    repos.
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
        total_repos = int(response_dict['total_count'])
        print(f"\tTotal repositories found: {total_repos}")
        return total_repos


def make_visualization(data_to_vis):
    """Based on given data makes comparison visualization for language."""
    data = [{
        'type': 'bar',
        'x': list(data_to_vis.keys()),
        'y': list(data_to_vis.values()),
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Repos count on GitHub by language comparison chart',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Language',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Repos count',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename=f'graphs/various_repos/repos_comparison.html')


# CREATE VISUALIZATION
language_list = ['Python', 'JavaScript', 'Ruby', 'C', 'Java', 'Perl',
                 'Haskell', 'Go', "C++", "Julia"]

create_language_comparison_visualization(language_list)