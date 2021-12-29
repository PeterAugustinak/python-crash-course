import requests
from plotly import offline


def create_submission_rank_visualization(number_of_submissions):
    submissions_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    submission_ids = get_api_data(submissions_url)
    titles, links, comments = get_info_from_submissions(submission_ids,
                                                        number_of_submissions)
    make_visualization([titles, links, comments])


def get_api_data(url):
    """Makes API-call and returns data dict."""

    # make an AP call and store the response
    r = requests.get(url)
    # print(f"Status code: {r.status_code}")

    # process information about each submission
    data_dict = r.json()
    return data_dict


def get_info_from_submissions(submission_ids, number_of_submissions):
    """Generates dictionary with given number of submissions."""

    titles, links, comments_num = [], [], []
    for submission_id in submission_ids[:number_of_submissions]:
        # make separate API-call for each submission
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        response_dict = get_api_data(url)

        title = response_dict['title']
        link = f"http://news.ycombinator.com/item?id={submission_id}"
        comment_num = response_dict.get('descendants', 0)

        titles.append(title)
        links.append(link)
        comments_num.append(comment_num)

    for title, link, comment in zip(titles, links, comments_num):
        print(f"{title} - {link} - {comment}")

    return titles, links, comments_num


# 17-2
def make_visualization(data_to_vis):
    """Creates visualization based on received data."""

    repo_links = [f"<a href='{link}'>{title[:10]} ...</a>" for link, title in
                  zip(data_to_vis[1], data_to_vis[0])]
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': data_to_vis[2],
    'hovertext': data_to_vis[0],
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Submission chart by number of comments',
        'titlefont': {'size': 20},
        'xaxis': {
            'title': '',
            'titlefont': {'size': 20},
            'tickfont': {'size': 14},
            'categoryorder': 'total descending',
            'side': 'bottom'
        },
        'yaxis': {
            'title': 'Number of comments',
            'titlefont': {'size': 20},
            'tickfont': {'size': 14},
        },
    }
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename=f'graphs/submission_chart.html')


create_submission_rank_visualization(30)

