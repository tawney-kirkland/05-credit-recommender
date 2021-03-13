import streamlit as st
import pickle
import numpy as np
import pandas as pd

import plotly.graph_objects as go
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
    
## Format app layout
    
st.set_page_config(layout='wide',initial_sidebar_state='auto')

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
    This site was created by Tawney Lott. You can find her on [GitHub](https://github.com/tawney-kirkland) and [LinkedIn](https://www.linkedin.com/in/tawney-lott-68230797/).
    '''
    
elif choice == 'App analysis':
    st.title('Understanding the apps included in the analysis')
    st.write('Text goes here')

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
        # Add an expander
        my_expander = st.beta_expander("Filter your recommendations", expanded=False)

        with my_expander:
            apps = name['genre'].unique()
            app_choice = st.selectbox('App category', apps)
            years = name["year"].unique()
            year_choice = st.selectbox('', years) 
            
        st.header("Check out these apps!")
        fig = go.Figure(data=[go.Table(
            columnorder = [1,2],
            columnwidth = [0.3,0.7],
            header=dict(values=['<b>App name</b>', '<b>Summary</b>'],
                        font = dict(color='black', size=18),
                        fill_color = 'white',
                        line_color = 'white',
                        align ='left',
                        height = 40),
            cells=dict(values=[name.title, name.summary],
                        font = dict(color='black', size=14),
                        fill_color = 'white',
                        line_color = 'white',
                        align = 'left',
                        height=40))
        ])
        
        fig.update_layout(width=1000,height=500)
        st.plotly_chart(fig)
        #st.dataframe((name[['title','description']][0:20]).reset_index(drop=True))

    