import re
import json

emoticons_str = r"""
    (?:
        [:=;] 
        [oO\-]? 
        [D\)\]\(\]/\\OpP]
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>',
    r'(?:@[\w_]+)', 
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", 
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',
    r"(?:[a-z][a-z'\-_]+[a-z])", 
    r'(?:[\w_]+)', 
    r'(?:\S)' 
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        # Convert all tokens (with alphabet characters) to lowercase
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens ]
    return tokens

# if __name__ == '__main__':
#   with open('tweets.json', 'r') as f:
#     for line in f:
#       if len(line.strip()) > 0:
#         tweet = json.loads(line)
#         tokens = preprocess(tweet['text'])
#         print(tokens)
