import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.set_page_config(layout='wide',initial_sidebar_state='auto')

choice = st.sidebar.radio("Navigation",('Home','App analysis','Give me an app recommendation'))

st.sidebar.write(
    '''
    __About__ \n
    This project was developed using approximately 22,000 apps scraped from the Google Play app store. 
    \n
    This site was created by Tawney Lott. You can find her on [GitHub](https://github.com/tawney-kirkland) and [LinkedIn](https://www.linkedin.com/in/tawney-lott-68230797/).
    ''')

# Create content for each page
if choice == 'Home':
    st.title('Google Play Store: App Analysis and Recommender')
    '''On the side bar on the left you will find a few different applications'''
    '''
    1. This is the __Home Page__
    2. View the __App analysis__ to learn more about the apps sampled from the Google Play Store
    3. Use the __Recommender__ app to find the type of app you are looking for
    '''
    
elif choice == 'App analysis':
    st.title('Understanding the apps included in the analysis')
    st.write('Text goes here')

elif choice == 'Give me an app recommendation':
    st.title("Use this recommender to find cool new apps")

        
    # Format inputs
    user_app_description = st.text_input("In a few words, describe the type of app you are looking for", '')
    text = [user_app_description]

    # And within an expander
    my_expander = st.beta_expander("Filter your recommendations", expanded=True)
    with my_expander:
        clicked = "By app category"
        
    st.subheader('Have a look at these apps')