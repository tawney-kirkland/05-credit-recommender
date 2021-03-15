import streamlit as st
import pickle
import numpy as np
import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html

from sklearn.decomposition import NMF
from sklearn.metrics import pairwise_distances

## Recommender pickles
with open('df_apps_topics.pkl', 'rb') as read_file:
    df_apps_topics = pickle.load(read_file)
    
with open('nmf_model.pkl', 'rb') as read_file:
    nmf_model = pickle.load(read_file)

with open('vectorizer.pkl', 'rb') as read_file:
    vectorizer = pickle.load(read_file)
    
with open('doc_topic_array.pkl', 'rb') as read_file:
    doc_topic = pickle.load(read_file)
    
df = pd.read_csv('04-data/preprocessed_app_data.csv')
    
## Format app layout
    
st.set_page_config(layout='wide',initial_sidebar_state='collapsed')

choice = st.sidebar.radio("Navigation",('Home','App analysis',"I'm looking for a new app!"))

# Create content for each page
if choice == 'Home':
    st.title('Google Play Store: App Analysis and Recommender')
    '''
    __About__ \n
    With over 3 million apps listed, the Google Play store provides a rich source for understanding some of the most important features of a successful app. While this volume of apps provides exciting opportunities for users to discover hidden gems, the sheer volume can be a bit overwhelming to navigate.
    \n
    Analyzing 22,000 apps scraped from the Google Play store, this project aims to provide insights for app developers to understand what types of apps users are looking for. 
    \n
    From a user perspective, the project aims to provide a fun resource which can be used to find cool apps.
    \n
    I am excited to have you here - use the navigation pane on the left of the page to explore!
    '''
    '''
    \n
    This site was created by Tawney Lott. You can find her on [GitHub](https://github.com/tawney-kirkland), [LinkedIn](https://www.linkedin.com/in/tawney-lott-68230797/) and [Medium](https://tawneyslott.medium.com/).
    '''
    
elif choice == 'App analysis':
    st.title('Understanding the apps included in the analysis')
    
    col1, col2 = st.beta_columns(2)
    with col1:
        col1.header("Original")
        df2 = df.groupby('genre')['genre'].count().reset_index(name='count')
        col1.fig = px.treemap(df2, path=['genre'], values='count')
        st.plotly_chart(col1.fig)
    
    with col2:
        col2.header("second figure goes here")
        #col2.image(grayscale, use_column_width=True)


elif choice == "I'm looking for a new app!":
    st.title("Use this recommender to find cool new apps")
        
    # Format inputs
    user_app_description = st.text_input("In a few words, describe the type of app you are looking for:", '')
    text = [user_app_description]
    tt = nmf_model.transform(vectorizer.transform(text))
    rec_array = pairwise_distances(tt.reshape(1,-1),doc_topic,metric='cosine').argsort()
    recs = list(rec_array[0][0:20])
    name = df_apps_topics.iloc[recs]
    name = name[0:15]
    
    
    st.write('\n')
    if user_app_description == '':
        st.write('''
        
        ''')
    else:
        st.spinner("Looking for apps...")
        # Add an expander
        my_expander = st.sidebar.beta_expander("Filter your recommendations here", expanded=True)

        with my_expander:
            apps = name['genre'].unique()
            apps = np.insert(apps,0,'Select one',axis=0)
            app_choice = st.selectbox('App category', apps)
            years = np.array(name["year"].unique(),dtype=object)
            years = np.sort(years)
            years = np.insert(years,0,'Select one',axis=0)
            year_choice = st.selectbox('Release year', years) 
            
        st.header("Check out these apps!")

        break_line = '<hr style="border:2px solid gray"> </hr>'
        st.markdown(break_line, unsafe_allow_html = True)
        st.write("") 
            
        for (idx,row) in name.iterrows():
            if app_choice == 'Select one' and year_choice == 'Select one':
                col1, mid, col2 = st.beta_columns([1,1,25])
                with col1:
                    st.image(row.loc['icon'], width=60)
                with col2:
                    st.subheader(row.loc['title'])
                value = row.loc['score']
                st.write('Stars:',round(value,2)) # Convert to stars?
                #st.markdown("<span class='stars'>value</span>", unsafe_allow_html = True)
                st.write(row.loc['summary'])
                link = row.loc['url']
                st.write("See more [here](link)")
                st.markdown(link, unsafe_allow_html=True)# Why isn't the URL working?
                break_line = '<hr style="border:2px solid gray"> </hr>'
                st.markdown(break_line, unsafe_allow_html = True)
            elif app_choice == row.loc['genre']:
                col1, mid, col2 = st.beta_columns([1,1,25])
                with col1:
                    st.image(row.loc['icon'], width=60)
                with col2:
                    st.subheader(row.loc['title'])
                value = row.loc['score']
                st.write('Stars:',round(value,2)) # Convert to stars?
                #st.markdown("<span class='stars'>value</span>", unsafe_allow_html = True)
                st.write(row.loc['summary'])
                st.write(row.loc['url']) # Why isn't the URL working?
                break_line = '<hr style="border:2px solid gray"> </hr>'
                st.markdown(break_line, unsafe_allow_html = True)
            
       