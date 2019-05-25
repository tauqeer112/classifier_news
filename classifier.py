# -*- coding: utf-8 -*-
import pickle
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
"""
Created on Tue May 21 15:31:11 2019

@author: Tauqeer
"""


import re
import nltk
import psycopg2


nltk.download('stopwords')


set(stopwords.words('english'))

hostname = 'pillar.cn575bdhhafi.ap-south-1.rds.amazonaws.com'  # host
username = 'pillar'  # username
password = 'save1950'  # your password
database = 'pillar'  # database name

with open('svm_model_linear_lite.pickle', 'rb') as f:
    svm_model_linear = pickle.load(f)


with open('tfidf_lite.pickle', 'rb') as f:
    tfidf = pickle.load(f)

with open('vectorizer_lite.pickle', 'rb') as f:
    vectorizer = pickle.load(f)


# X = vectorizer.transform(X).toarray()
# tfidf.transform(X).toarray()
# svm_predictions = svm_model_linear.predict(X)
#
# svm_pridictions = svm_predictions.tolist()
#
# pred = svm_pridictions[0]
# print(pred)


'''Categorization'''

connection = psycopg2.connect(
    host=hostname, user=username, password=password, dbname=database)
cur = connection.cursor()

""" republic"""

cur.execute("SELECT headline, link , category from feed_republic")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_republic set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""DNA"""

cur.execute("SELECT headline, link , category from feed_dna")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_dna set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""IndiaTv"""

cur.execute("SELECT headline, link , category from feed_indiatv")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_indiatv set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""News18"""

cur.execute("SELECT headline, link , category from feed_news18")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_news18 set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""firstpost"""

cur.execute("SELECT headline, link , category from feed_firstpost")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_firstpost set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""indianExpress"""

cur.execute("SELECT headline, link , category from feed_indianexpress")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_indianexpress set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""Ndtv"""


cur.execute("SELECT headline, link , category from feed_ndtv")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_ndtv set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""oneindia"""


cur.execute("SELECT headline, link , category from feed_oneindia")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_oneindia set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""thehindu"""


cur.execute("SELECT headline, link , category from feed_thehindu")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_thehindu set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

"""zee"""


cur.execute("SELECT headline, link , category from feed_zeenews")
rows = cur.fetchall()
for row in rows:
    if(row[2] == None):
        X = [row[0] + " " + row[1]]
        news = re.sub('[^a-zA-Z]', ' ', X[0])
        news = news.lower()
        news = news.split()
        ps = PorterStemmer()
        news = [word for word in news if not word in {
            'http', 'www', 'dnaindia', 'com', 'zeenews', 'oneindia', 'ndtv', 'firstpost', 'news18', 'republicworld', 'thehindu'}]
        news = [ps.stem(word)
                for word in news if not word in set(stopwords.words('english'))]

        news = ' '.join(news)
        X = [news]
        X = vectorizer.transform(X).toarray()
        tfidf.transform(X).toarray()
        svm_predictions = svm_model_linear.predict(X)

        svm_pridictions = svm_predictions.tolist()

        pred = svm_pridictions[0]
        print(row[1] + " : " + pred)

        try:
            cur.execute(
                "UPDATE feed_zeenews set category = %s where link = %s", (pred, row[1]))
            connection.commit()
        except Exception as ex:
            cur.execute("ROLLBACK")
            connection.commit()

cur.close()
connection.close()
