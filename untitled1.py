# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 01:18:50 2019

@author: hossein
"""

import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.read_csv('ml-latest-small/ratings.csv')

movie_names = pd.read_csv('ml-latest-small/movies.csv')

movie_names.head()

ratings.head()

movies_and_ratings = pd.merge(ratings,movie_names , on='movieId')


movies_and_ratings.head()


user_movie_rating = movies_and_ratings.pivot_table(index='userId', columns='title', values='rating')



user_movie_rating.head()

user_movie_rating = user_movie_rating.fillna(0)


def standarize(row):
    new_row = (row -row.mean()) / (row.max()-row.min())
    return new_row

ratings_std = user_movie_rating.apply(standarize)


item_similarity = cosine_similarity(ratings_std)




