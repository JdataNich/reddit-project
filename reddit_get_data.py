import reddit_request
import requests
import os

REDDIT_USERNAME = os.environ.get('REDDIT_USERNAME')
REDDIT_PASS = os.environ.get('REDDIT_PASS')
APP_ID = os.environ.get('APP_ID')
APP_SECRET = os.environ.get('APP_SECRET')

def get_subreddit_data(subreddit, auth):
    
    token = 'bearer ' + auth['access_token']
    headers = {'Authorization': token, 'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
    api_url = 'https://oauth.reddit.com'
    payload = {'q': subreddit, 'limit': 5, 'sort': 'relevance'}
    response = requests.get(api_url + '/subreddits/search', headers=headers, params=payload)
    
    return response
# %%
auth = reddit_request.reddit_auth(REDDIT_USERNAME, REDDIT_PASS, APP_ID, APP_SECRET)
response = get_subreddit_data('gamestop', auth)
data = response.json()['data']
print(data)
