import os
import pickle

path_npa = (r'C:\Users\Ильяс\texts\npa')
path_tz = (r'C:\Users\Ильяс\texts\tz')
docs_npa = os.listdir(path_npa)
docs_tz = os.listdir(path_tz)
words = []
npas = 0
tzs = 0

for doc in docs_npa:
    fullpath = os.path.join(path_npa, doc)
    f = open(fullpath, 'r')
    text = f.read()
    words.append(text)
    f.close()
    npas += 1
    
for doc in docs_tz:
    fullpath = os.path.join(path_tz, doc)
    f = open(fullpath, 'r')
    text = f.read()
    words.append(text)
    f.close()
    tzs += 1

targets = ['npa']*npas + ['tz']*tzs

import sklearn
from sklearn import model_selection
data_train, data_test, targets_train, targets_test = sklearn.model_selection.train_test_split(words, targets, test_size = 0.3)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
data_train_count = vectorizer.fit_transform(data_train)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
data_train_tfidf = tfidf_transformer.fit_transform(data_train_count)

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('text_clf', MultinomialNB()),
])
clf.fit(data_train, targets_train)
with open('my_classifier.pkl', 'wb') as pickle_file:
    pickle.dump(clf, pickle_file)
predicted = clf.predict(data_test)

import numpy as np
p = np.mean(predicted == targets_test)
print('accuracy = {acc}'.format(acc=p))


