import requests
import os

REDDIT_USERNAME = os.environ.get('REDDIT_USERNAME')
REDDIT_PASS = os.environ.get('REDDIT_PASS')
APP_ID = os.environ.get('APP_ID')
APP_SECRET = os.environ.get('APP_SECRET')

# TODO: this could possibly be a class
def reddit_auth(username, pword, app_id, app_secret):
    '''
    This function returns a dictionary containing an access token
    for reddit to be used in future requests
    '''
    base_url = 'https://www.reddit.com/'
    data = {
        'grant_type': 'password',
        'username': username,
        'password': pword
        }

    auth = requests.auth.HTTPBasicAuth(app_id, app_secret)
    resp = requests.post(base_url + 'api/v1/access_token',
                    data=data,
                    headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
                    auth=auth)
    auth_token = resp.json()

    return auth_token
