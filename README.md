# 05-google-play

This repo is for Metis project 5

## Background

With over 3 million apps, the Google Play store is a rich resource for app developers and users. The volume of apps is massive and has continusously grown since 2010.

## Objective

* Analyze Google Play App store data for a sample of ~ 22,000 apps to predict the user rating for each app
* Develop an app recommendation engine using content-based filtering

## Methods
* **Desktop review** of Google Play Store news and similar studies
* **Exploratory data analysis** of semi-structured and unstructured data gathered from the Google Play store
* **Linear regression** to predict the average user rating of apps 
* **Sentiment analysis** of user reviews as an input into the regression analysis
* **Recommender system** for users looking for interesting apps

## Findings

#### Topic modeling and sentiment analysis of user reviews
Topic modeling of approximately 2 million user reviews revealed seven core topics and the top words within each topic.

To be updated with images

#### Predicting app ratings using linear regression

The model explains 31% of variance in user ratings. On average, predictions are 0.28 above or below the true app rating.

#### Recommender system
To be updated with demo video

## Insights

* User sentiment regarding **Features is strongest predictor of ratings** - give the user what they want
* Payments results suggests there is an **opportunity to improve payments experience** and process for apps
* Apps by **Top Developers tend to have better ratings** - important to establish and maintain brand
* Apps that are **free and do not contain ads tend to have lower scores** - serious developers should investigate ads and / or payment models

## Tools
* Python
* Jupyter Notebook
* Google-play-scraper
* Pandas
* Numpy
* NLTK
* NMF
* Linear regression
* Random Forest
* Matplotlib
* Seaborn
* Tableau
* Streamlit