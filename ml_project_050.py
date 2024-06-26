# -*- coding: utf-8 -*-
"""ML PROJECT-050.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1inMYY7BbnK7TV9RRvZF_YGklxgACsgzm

NAME : AALAP DAVE

My dataset is to predict quality of wine . For this task I will be performing eda and preprocessing of given data

Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

"""#Dataset Collection"""

#reading thecsv file of wine quality dataset
df = pd.read_csv("/content/winequality-red.csv")

df.head()

# number of rows & columns in the dataset
df.shape

df.isnull().sum()

"""As there is no missing values in this dataset we don't need to drop any rows

#Exploratory data analysis (EDA)
"""

df.describe()

sns.catplot(x='quality', data = df, kind = 'count')

"""This graph indicates number of values for each quality .
Quality value is directly propotional to count. hence if more the count better the quality of wine
"""

# volatile acidity vs Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x='quality', y = 'volatile acidity', data = df)

"""Here we can infer that volatile acidity is inversely propotional to quality"""

# citric acid vs Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x='quality', y = 'citric acid', data = df)

"""We can infer citric acid and quality are directly propotional"""

# density vs Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x='quality', y = 'density', data = df)

"""Correlation:"""

correlation = df.corr()

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt = '.1f', annot = True, annot_kws={'size':8}, cmap = 'Reds')

"""#DATA PREPROCESSING"""

X = df.drop('quality',axis=1)

print(X)

Y = df['quality'].apply(lambda y_value: 1 if y_value>=7 else 0)
print(Y)

"""Required EDA is performed to understand following dataset in terms of quality with respect to various factors such as citric acid,sugar,density. Data cleaning  and label binarization is done.

#Train and test split
"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

print(Y.shape, Y_train.shape, Y_test.shape)

"""It depicts out of 1599 values in my dataset , out of which 1279 are used for training and 320 values are used for testing."""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""#Model Training:

#Random Forest Classifier
"""

model = RandomForestClassifier()

model.fit(X_train, Y_train)

"""Here we have used Random Forest method for achieving optimum accuracy score for this dataset.

Accuracy score
"""

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy : ', test_data_accuracy)

"""Hence we achieve accuracy score of 0.93 ."""

#Logistic Regression
from sklearn.linear_model import LogisticRegression
model1 = LogisticRegression()
model1.fit(X_train, Y_train)
# Accuracy score
test_data_accuracy1 = accuracy_score(model1.predict(X_test), Y_test)
print('Accuracy : ', test_data_accuracy1)

#SVM
from sklearn import svm
model2 = svm.SVC()
model2.fit(X_train, Y_train)
# Accuracy score
test_data_accuracy2 = accuracy_score(model2.predict(X_test), Y_test)
print('Accuracy : ', test_data_accuracy2)

#KNN
from sklearn.neighbors import KNeighborsClassifier
model3 = KNeighborsClassifier(n_neighbors=3)
model3.fit(X_train, Y_train)
# Accuracy score
test_data_accuracy3 = accuracy_score(model3.predict(X_test), Y_test)
print('Accuracy : ', test_data_accuracy3)

"""After training  the model using Logistic regression ,SVM and KNN we can see the accuracy score is not better than in random forest. Hence we go ahead with random forest classifier.

Building a Predictive System
"""

input_data = (7.5,0.5,0.36,6.1,0.071,17.0,102.0,0.9978,3.35,0.8,10.5)

# changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the data as we are predicting the label for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==1):
  print('Good Quality Wine')
else:
  print('Bad Quality Wine')

# prompt: saving  the above model to disk

import pickle

# Save the model to a file
with open('model.pkl', 'wb') as file:
  pickle.dump(model, file)

# Load the model from the file
with open('model.pkl', 'rb') as file:
  model = pickle.load(file)

"""Conclusion: The model predicts whether the quality of wine is good or bad according to the data provided by dataset. If the overall score is above 7 we classify it as good quality wine.

This predictive tool not only enhances our understanding of the complex factors influencing wine quality but also empowers winemakers and enthusiasts to make informed decisions.
"""