# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 07:16:53 2020

@author: hossein
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel , linear_kernel
import numpy as np

ratings = pd.read_csv('food_ratings.csv')
all_recipies = pd.read_csv('all_recipes.csv')
recipes_and_ratings = pd.merge(ratings , all_recipies , on='recipe_id')
#recipes_and_ratings =recipes_and_ratings.pivot_table(index='recipe_id', columns='title', values='category')

fooddf = recipes_and_ratings.set_index('recipe_id').reset_index().drop_duplicates(subset='recipe_id')


fooddf = fooddf.set_index('title')





tfv = TfidfVectorizer(min_df=3,max_features=None , strip_accents='unicode',analyzer='word',token_pattern=r'\w{1,}[^0-9]',ngram_range=(1,3),stop_words='english')

fooddf['ingredients'] = fooddf['ingredients'].fillna('')


tfv_matrix = tfv.fit_transform(fooddf['ingredients'])

fooddf = fooddf.reset_index()
sig = sigmoid_kernel(tfv_matrix,tfv_matrix)
#linear_model = linear_kernel(tfv_matrix,tfv_matrix)
indecies = pd.Series(fooddf.index ,index=fooddf['title'])

id_food = indecies['Ropa Vieja (Cuban Beef)']

sig_scores = list(enumerate(sig[id_food]))

sig_scores = sorted(sig_scores , key=lambda x:x[1],reverse=True)

def get_similar_food_ingredient(food_name ):
    fooddf = pd.read_csv('ingreadients_and_recipeNmaes.csv')
    indecies = pd.Series(fooddf.index ,index=fooddf['title'])
    idx = indecies[food_name]
    sig = np.array(pd.read_csv('ingredients_sig.csv'))
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores , key=lambda x:x[1],reverse=True)
#    return    sig_scores

    sig_scores = sig_scores[1:11]
    

    food_indicies = [i[0] for i in sig_scores]
    
    return fooddf['title'].iloc[food_indicies]

x2 = get_similar_food_ingredient('Ropa Vieja (Cuban Beef)')    



indecies = pd.Series(x2.index ,index=x2['title'])
idx = indecies[['Cherry Folditup','"Instant" Mac and Cheese']]
sig_scores = list(enumerate(sig[idx]))

sig_scores = sorted(sig_scores , key=lambda x:x[1].all(),reverse=True)

aryy = sig_scores[0][1]
