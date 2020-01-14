# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 19:48:34 2019

@author: hossein
"""


import pandas as pd
#from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity



ratings = pd.read_csv('food_ratings.csv')
recipes_names = pd.read_csv('all_recipes.csv').drop_duplicates(subset='title')
recipes_and_ratings = pd.merge(ratings , recipes_names , on='recipe_id')

better_user_ratings = recipes_and_ratings.pivot_table(index='title',columns='user_id',values='rating')
better_user_ratings = better_user_ratings.dropna(thresh=4 , axis=1)


my_user_list = better_user_ratings.columns.tolist()

recipes_and_ratings = recipes_and_ratings.loc[recipes_and_ratings['user_id'].isin(my_user_list)]

#recipes_and_ratings = pd.merge(ratings , recipes_names , on='recipe_id')
##################################################

recipes_titles= recipes_names['title'].str.replace('"','').tolist()

#for i in range(len(recipes_titles)):
#    recipes_titles[i] = recipes_titles[i].replace('"','')




##################################################

recipes_and_ratings =recipes_and_ratings.pivot_table(index='user_id', columns='title', values='rating')

recipes_and_ratings.head()

recipes_and_ratings = recipes_and_ratings.fillna(0)

def standarize(row):
    new_row = (row -row.mean()) / (row.max()-row.min())
    return new_row


recipes_and_ratings = recipes_and_ratings.apply(standarize)

recipes_and_ratings = recipes_and_ratings.iloc[0:1151,:]

item_similarity = cosine_similarity(recipes_and_ratings)
item_similarity = pd.DataFrame(item_similarity,columns=recipes_titles,index=recipes_titles)
item_similarity = item_similarity.to_csv('item_similarity_cosine.csv')
##################################################










def get_similarity(food_name ,user_rating):
    item_similarity = pd.read_csv('item_similarity_cosine.csv',index_col=0)
#    item_similarity.reset_index(item_similarity.columns.tolist())
#    return item_similarity
    similar_score = item_similarity[food_name]*(user_rating-2.5)

    similar_score = similar_score.sort_values(ascending=False)
    
    return similar_score.iloc[1:11]


x2 = get_similarity("Chef John's Carrot Cake",5)

x2 = x.reset_columns()


similar = item_similarity.loc['"Burnt" Basque Cheesecake']
columns_test = item_similarity.columns.tolist()
index_test = item_similarity.index.tolist()

new_list = list(dict.fromkeys(index_test))

for i in new_list:
    if i =="Kouign-Amann":
        print('fuck yes')

