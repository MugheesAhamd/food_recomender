# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:56:58 2020

@author: hossein
"""

import numpy as np
import pandas as pd


ratings = pd.read_csv('food_ratings.csv')
recipe_names = pd.read_csv('all_recipes.csv')

merges = pd.merge(ratings , recipe_names , on='recipe_id')

x = merges.groupby(['title'])['rating'].agg(['count'])





