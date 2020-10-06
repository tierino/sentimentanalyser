import pickle
import nlp_test
import json
from nltk import classify

import preprocessing

neg_count = pos_count = 0

with open('classifier', 'rb') as infile:
  classifier = pickle.load(infile)

with open('tweets.json', 'r') as f:
  for line in f:
    if len(line.strip()) > 0:
      tweet = json.loads(line)
      terms = [term for term in preprocessing.preprocess(tweet['text'], True)]
      cleaned_terms = nlp_test.remove_noise(terms)
     
      if classifier.classify(dict([term, True] for term in cleaned_terms)) == "Positive":
        pos_count += 1
      else:
        neg_count += 1

total = neg_count + pos_count
print("Negative:", format((neg_count / total) * 100, '.2f') + "%", "\nPositive:", format((pos_count / total) * 100, '.2f') + "%")
