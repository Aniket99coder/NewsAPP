import streamlit as st
import urllib.request as request
import json
from PIL import Image
import requests
import webbrowser




def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")
import pandas as pd
from newsapi import NewsApiClient
from datetime import date,timedelta

#Taking the search result
user_search = st.text_input("Search NEWS", "india")
q=user_search

newsapi = NewsApiClient(api_key='57822bea4e8c40bb8f7de63e9c9c7c65')


#Adding a slider 
num_news = st.sidebar.slider('Hey how many headline do you want to see?', 1, 8, 1)
st.write("*I want", num_news, 'headlines*')


json_data = newsapi.get_everything(q=user_search,
                                    language='en',
                                    from_param=str(date.today() -timedelta(days=29)),
                                    to= str(date.today()),
                                    sources = 'usa-today',
                                    page_size=100,
                                    page = 1,
                                   sort_by='relevancy'
                                    )
data = pd.DataFrame(json_data['articles'])




st.header('***Hello,these are the top news today for you! *** :sunglasses:')

#st.sidebar.write(data['description'][0])
for i in range(num_news):
	
	url=data['urlToImage'][i]
	text=data['description'][i]
	response=requests.get(url,stream=True)
	img=Image.open(response.raw)
	st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
	st.subheader(text)
	st.image(img, caption=data['title'][i],use_column_width=True)
	url_news=data['url'][i]
	if st.button('Read More about it',key=i):
	    webbrowser.open_new_tab(url_news)
	
	


