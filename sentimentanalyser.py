import config
from twython import Twython
import pandas as pd

twitter = Twython(config.API_KEY, config.API_SECRET)
auth = twitter.get_authentication_tokens()

base_query_term = "tottenham"
max_iters = 50

dict_ = {'id': [], 'date': [], 'text': [], 'retweet_count': [],
         'favorite_count': [], 'location': []}

max_id = ""
for call in range(0, max_iters):
    query = {
        'q': base_query_term,
        'result_type': 'recent',
        'count': 100,
        'lang': 'en',
        'max_id': max_id,  # what tweet id to start retrieving from
        'tweet_mode': 'extended',
        'include_entities': False
    }

for status in twitter.search(**query)['statuses']:
    if 'RT @' not in (status['full_text']):
        dict_['id'].append(status['id'])
        # dict_['user'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        dict_['text'].append(status['full_text'])  # > 128 chars
        dict_['favorite_count'].append(status['favorite_count'])
        dict_['retweet_count'].append(status['retweet_count'])
        dict_['location'].append(status['user']['location'])
        max_id = status['id']  # store last tweet accessed

df = pd.DataFrame(dict_)
df.sort_values(by='id', inplace=True, ascending=False)
print(df)
