# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 07:02:53 2020

@author: hossein
"""


import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.read_csv('ml-latest-small/ratings.csv')

movie_names = pd.read_csv('ml-latest-small/movies.csv')

ratings = pd.merge(movie_names , ratings ).drop(['genres','timestamp'],axis=1)

user_ratings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating').fillna(0)


item_similarity = user_ratings.corr(method='pearson')


def get_similarity(movie_name ,user_rating):
    similar_score = item_similarity[movie_name]*(user_rating-2.5)
    print(similar_score)
    similar_score = similar_score.sort_values(ascending=False)
    
    return similar_score

print(get_similarity('Deadpool (2016)',5))

movies = [('Deadpool (2016)',5),("Godfather: Part II, The (1974)",5),("Godfather, The (1972)",5)]

similar_movies = pd.DataFrame()

for movie,rating in movies:
    similar_movies = similar_movies.append(get_similarity(movie,rating),ignore_index=True)

x = similar_movies.sum().sort_values(ascending=False)
