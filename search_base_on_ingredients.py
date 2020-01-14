# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:05:06 2020

@author: hossein
"""

import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import operator


recipes = pd.read_csv('all_recipes.csv')



#####################stop words and cleaning the data#######################

recipes['ingredients'] = recipes['ingredients'].str.replace('\d+','')
recipes['ingredients'] = recipes['ingredients'].str.replace('/','')
recipes['ingredients'] = recipes['ingredients'].str.replace('(','')
recipes['ingredients'] = recipes['ingredients'].str.replace(')','')
recipes['ingredients'] = recipes['ingredients'].str.replace('-','')
recipes['ingredients'] = recipes['ingredients'].str.replace('\\','')
recipes['ingredients'] = recipes['ingredients'].str.replace('[','')
recipes['ingredients'] = recipes['ingredients'].str.replace(']','')
recipes['ingredients'] = recipes['ingredients'].str.replace('"','')
recipes['ingredients'] = recipes['ingredients'].str.replace("'",'')

words_removed = ['cup','cups','ounce','package','teaspoon','spoon','pepper','taste','tablespoons','salt','teaspoons','needed','cut','pound','optional','pounds']
STOP_WORDS = nltk.corpus.stopwords.words('english')
STOP_WORDS.extend(words_removed)
stop = set(STOP_WORDS)


pat = r'\b(?:{})\b'.format('|'.join(stop))
recipes['ingredients'] = recipes['ingredients'].str.replace(pat, '')



#################bag of words ##############################################


text_data = recipes['ingredients']
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)
bag_of_words.toarray()
feature_names = count.get_feature_names()
words_count_array = bag_of_words.toarray().sum(axis=0)
words_in_dict = dict(zip(words_count_array , feature_names))
words_in_dict = sorted(words_in_dict.items() , key=operator.itemgetter(0))




