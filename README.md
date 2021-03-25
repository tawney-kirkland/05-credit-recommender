# 05-google-play

This repo is for Metis project 5

## Background

With over 3 million apps, the Google Play store is a rich resource for app developers and users. The volume of apps is massive and has continusously grown since 2010.

## Objective

Against this backdrop, the project aimed to address the following objectives:
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
Topic modeling of approximately 2 million user reviews revealed seven core topics and the top words within each topic, as shown in the table below. This analysis was really helpful as it enabled me to integrate details related to app experience and usability.

<img width="900" alt="topics_table" src="https://user-images.githubusercontent.com/74927862/112393397-5f4f0600-8cd1-11eb-88df-8cc01fd85c06.png">

Sentiment analysis of user reviews was used to provide an additional layer of insight across the seven topics. The figure below shows the sentiment split for each of the review topics.

<img width="800" alt="sentiment_by_topic" src="https://user-images.githubusercontent.com/74927862/112393532-9de4c080-8cd1-11eb-828e-fcdd6f423218.png">

Interestingly, The Payments topic has a larger share of negative reviews than Bugs, suggesting an opportunity to improve Payments experience for the apps in this analysis.

#### Predicting app ratings using linear regression

The model explains 31% of variance in user ratings. On average, predictions are 0.28 above or below the true app rating.

The figure below indicates some of the strongest positive and negative predictors of app ratings.

<img width="800" alt="coefficients" src="https://user-images.githubusercontent.com/74927862/112393572-ad640980-8cd1-11eb-9fd8-52cb3f25c77d.png">

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
