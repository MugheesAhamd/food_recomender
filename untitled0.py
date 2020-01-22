# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:00:28 2020

@author: hossein
"""

#mean absolute error


import pandas as pd
import math

ratings = pd.read_csv('food_ratings.csv')
recipes_names = pd.read_csv('all_recipes.csv').drop_duplicates(subset='title')
recipes_names['title'] = recipes_names['title'].str.replace('"','')
recipes_and_ratings = pd.merge(ratings , recipes_names , on='recipe_id')
item_similarity = pd.read_csv('item_similarity_cosine.csv',index_col=0)

#test = ratings['recipe_id'].unique()

item_similarity_index = item_similarity.index.tolist()
#ratings = ratings[~ratings['recipe_id'].isin([222234])]


def get_similarity(food_name ,user_rating):
#    item_similarity.reset_index(item_similarity.columns.tolist())
#    return item_similarity
    similar_score = item_similarity[food_name]*(user_rating-2.5)

    #similar_score = similar_score.sort_values(ascending=False)
    
    return similar_score



user_idies = ratings['user_id']
ratings = ratings.set_index('user_id')


recipes_names = recipes_names.set_index('recipe_id')

predictions = []
true_values = []
error = []
ratings_df = []
i=0
for user_id in user_idies:

    if ratings.loc[[user_id]].shape[0]>=2:
        user_rated_df_original = ratings.loc[[user_id]].reset_index()
        user_rated_df_droped_first_row = user_rated_df_original.drop(0)
        for index in user_rated_df_droped_first_row.index:
            try:
                ratings_df.append(get_similarity(recipes_names.loc[[user_rated_df_droped_first_row.loc[[index]]['recipe_id'][index]]]['title'],user_rated_df_droped_first_row.loc[[index]]['rating'][index]))
            except:
                print('errrrrrrrrrrrrrrrrrrrrrrrror')
                print(i)
                print(user_rated_df_droped_first_row.loc[[index]]['recipe_id'][index])
        ratings_df = pd.concat(ratings_df,axis=1).sum(axis=1)
        user_rated_first_row = user_rated_df_original.loc[[0]]
        food_name = recipes_names.loc[user_rated_first_row['recipe_id'][0]]
        predictions.append(ratings_df.loc[food_name['title']]+2.5)
        true_values.append(user_rated_first_row['rating'][0])
        ratings_df = []
        
        i +=1
        pass
    #if i >5:
     #   break



i = 0 
while i <= len(predictions):
    error.append(abs(predictions[i-1] - true_values[i-1])**2)
    i+=1

error = sum(error)
error = error/6201
error = math.sqrt(error)

